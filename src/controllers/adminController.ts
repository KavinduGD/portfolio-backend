import { Request, Response } from "express";
import asyncHandler from "express-async-handler";
import Admin from "../models/adminModel";
import User from "../models/userModel";
import bcrypt from "bcrypt";
import { generateToken } from "../utils/generateToken";

const login = asyncHandler(async (req: Request, res: Response) => {
  const { email, password } = req.body;

  if (!email || !password) {
    res.status(400);
    throw new Error("Email and password required");
  }

  const admin = await Admin.findOne();

  //  id admin collection empty
  if (!admin) {
    res.status(404);
    throw new Error("Admin data cannot be found in database");
  }

  // check admin email and user entered email
  if (admin.email !== email) {
    res.status(400);
    throw new Error("Email is Invalid");
  }

  // check password
  const isPasswordMatched = await bcrypt.compare(password, admin.password);

  if (!isPasswordMatched) {
    res.status(400);
    throw new Error("Password is Invalid");
  }

  const token = generateToken(admin._id.toString());

  res.cookie("admin_token", token, {
    httpOnly: true, // JS cannot access (XSS protection)
    secure: process.env.NODE_ENV === "production", // HTTPS only
    sameSite: "strict", // CSRF protection
    maxAge: 7 * 24 * 60 * 60 * 1000, // 7 days
  });

  res.status(200).json({
    message: "User logged in successfully",
  });
});

export { login };
