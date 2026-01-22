import express from "express";
import {
  addCertificate,
  deleteCertificate,
  getCertificates,
  updateCertificate,
} from "../controllers/certificateController";
import adminValidator from "../middleware/authMiddleware";
import createUploader from "../utils/upload";

const certificateImageUploader = createUploader("certificate", 5);

const router = express.Router();

router.get("/", getCertificates);
router.post(
  "/",
  adminValidator,
  certificateImageUploader.single("certificate-image"),
  addCertificate,
);
router.patch(
  "/:id",
  adminValidator,
  certificateImageUploader.single("certificate-image"),
  updateCertificate,
);
router.delete("/:id", adminValidator, deleteCertificate);

export default router;
