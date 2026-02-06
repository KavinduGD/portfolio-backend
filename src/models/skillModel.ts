import mongoose from "mongoose";
import { ISkill } from "../types/types";

const skillSchema = new mongoose.Schema<ISkill>({
  skill: {
    type: String,
    required: true,
    unique: true,
  },
  skillImage: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
});

const Skill = mongoose.model<ISkill>("Skill", skillSchema);

export default Skill;
