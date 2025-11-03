def compose_address_block(fullname, address_line1, subdistrict, district, province, postcode, phone=None):
    lines = []
    if fullname:
        lines.append(fullname)
    addr_line = " ".join(x for x in [
        address_line1,
        f"ต.{subdistrict}" if subdistrict else None,
        f"อ.{district}" if district else None,
        f"จ.{province}" if province else None,
        str(postcode) if postcode else None
    ] if x)
    if addr_line:
        lines.append(addr_line)
    if phone:
        lines.append(f"โทร {phone}")
    return "\n".join(lines)
