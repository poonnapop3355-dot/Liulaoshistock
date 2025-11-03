from fastapi import APIRouter, Depends
from typing import List
from app.schemas.order import Order
from app.core.rbac import require_role
from app.core.helpers import compose_address_block
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.post("/labels", response_class=HTMLResponse, dependencies=[Depends(require_role(["admin", "manager", "packer"]))])
def create_shipping_labels(orders: List[Order]):
    """
    Generate an HTML document for an A4 sheet with 3x2 text-only shipping labels.
    """
    labels_html = ""
    for order in orders:
        address_block = compose_address_block(
            fullname=order.customer.fullname,
            address_line1=order.customer.address_line1,
            subdistrict=order.customer.subdistrict,
            district=order.customer.district,
            province=order.customer.province,
            postcode=order.customer.postcode,
            phone=order.customer.phone
        )
        labels_html += f"""
        <div class="label">
            <div class="addr">{address_block}</div>
        </div>
        """

    html_content = f"""
    <!doctype html>
    <html lang="th">
    <head>
    <meta charset="utf-8" />
    <title>Labels A4 3x2 – TEXT ONLY</title>
    <style>
      @page {{ size: A4; margin: 10mm; }}
      * {{ box-sizing: border-box; }}
      body {{ margin: 0; font-family: "Noto Sans Thai", Arial, sans-serif; }}
      .sheet {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: repeat(2, 1fr);
        gap: 5mm;
        height: calc(297mm - 20mm);
      }}
      .label {{
        padding: 6mm;
        font-size: 11pt;
        line-height: 1.25;
        display: flex; align-items: center; justify-content: flex-start;
      }}
      .addr {{ white-space: pre-line; word-break: break-word; }}
      @media print {{ .no-print {{ display: none; }} }}
    </style>
    </head>
    <body>
    <div class="sheet">
      {labels_html}
    </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
