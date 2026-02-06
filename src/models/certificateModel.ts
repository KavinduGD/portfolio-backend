import mongoose from "mongoose";
import type { ICertificate } from "../types/types";

const certificateSchema = new mongoose.Schema<ICertificate>({
  name: {
    type: String,
    unique: true,
    required: true,
  },

  issuer: {
    type: String,
    required: true,
  },
  issueDate: {
    type: String,
    required: true,
  },
  certificateImage: {
    type: String,
    required: true,
  },
  credentialsId: {
    type: String,
    required: true,
  },
  certificateLink: {
    type: String,
    required: true,
  },
  tags: {
    type: [String],
    required: true,
  },
  score: {
    type: Number,
    required: true,
  },
});

const Certificate = mongoose.model<ICertificate>(
  "Certificate",
  certificateSchema,
);

export default Certificate;
