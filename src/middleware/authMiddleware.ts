import { NextFunction, Request, Response } from "express";
import jwt from "jsonwebtoken";
import Admin from "../models/adminModel";
import asyncHandler from "express-async-handler";

const adminValidator = asyncHandler(
  async (req: Request, res: Response, next: NextFunction) => {
    const token = req.cookies.admin_token;

    if (!token) {
      res.status(401);
      throw new Error("Not authorized");
    }

    const decoded = jwt.verify(token, process.env.JWT_SECRET!) as {
      id: string;
    };

    const admin = await Admin.findById(decoded.id);

    if (!admin) {
      res.status(401);
      throw new Error("Not authorized");
    }

    next();
  },
);

export default adminValidator;
