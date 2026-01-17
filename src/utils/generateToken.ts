import jwt from "jsonwebtoken";

export const generateToken = (adminId: string) => {
  return jwt.sign(
    { id: adminId }, // payload
    process.env.JWT_SECRET!, // secret key
    { expiresIn: "7d" }, // token lifetime
  );
};
