import express from "express";
import {
  getSkills,
  addSkill,
  updateSkill,
  deleteSkill,
} from "../controllers/skillController";
import adminValidator from "../middleware/authMiddleware";
import createUploader from "../utils/upload";

const skillImageUploader = createUploader("skill", 5);

const router = express.Router();

router.get("/", getSkills);
router.post(
  "/",
  adminValidator,
  skillImageUploader.single("skill-image"),
  addSkill,
);
router.patch(
  "/:id",
  adminValidator,
  skillImageUploader.single("skill-image"),
  updateSkill,
);
router.delete("/:id", adminValidator, deleteSkill);

export default router;
