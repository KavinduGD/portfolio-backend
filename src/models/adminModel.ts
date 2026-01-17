import mongoose from "mongoose";
import type { IAdmin } from "../types/types";
import bcrypt from "bcrypt";
import { NextFunction } from "express";

const adminSchema = new mongoose.Schema<IAdmin>({
  email: {
    type: String,
    required: true,
  },
  password: {
    type: String,
    required: true,
  },
});

adminSchema.pre("save", async function () {
  if (!this.isModified("password")) {
    return;
  }
  const salt = await bcrypt.genSalt(10);
  this.password = await bcrypt.hash(this.password, salt);
});

const Admin = mongoose.model<IAdmin>("Admin", adminSchema);

export default Admin;
