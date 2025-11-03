// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAnHYatkHbK_S59BoZVHDz56YHoOwvoO7I",
  authDomain: "liulaoshistock.firebaseapp.com",
  databaseURL: "https://liulaoshistock-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "liulaoshistock",
  storageBucket: "liulaoshistock.firebasestorage.app",
  messagingSenderId: "1059566282555",
  appId: "1:1059566282555:web:ddb4bee395d9dd3e1fb91e",
  measurementId: "G-N4WFGD075S"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
