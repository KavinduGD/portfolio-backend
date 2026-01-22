import multer from "multer";
import path from "path";
import fs from "fs";
import { v4 as uuidv4 } from "uuid";

const createUploader = (folderName: string, maximumFileSize: number) => {
  const uploadPath = path.join(process.cwd(), "uploads", folderName);

  // ensure folder exists
  if (!fs.existsSync(uploadPath)) {
    fs.mkdirSync(uploadPath, { recursive: true });
  }

  const storage = multer.diskStorage({
    destination: uploadPath,

    filename: (req, file, cb) => {
      const baseName = file.fieldname.toLowerCase().replace(/\s+/g, "-");

      const uniqueId = uuidv4();
      const ext = path.extname(file.originalname);

      cb(null, `${baseName}-${uniqueId}${ext}`);
    },
  });

  // 2. Define the File Filter
  const fileFilter: multer.Options["fileFilter"] = (req, file, cb) => {
    if (file.mimetype.startsWith("image/")) {
      cb(null, true);
    } else {
      cb(new Error("Only image files are allowed"));
    }
  };

  const uploader = multer({
    storage: storage,
    fileFilter: fileFilter,
    limits: {
      fileSize: 1024 * 1024 * maximumFileSize,
    },
  });
  return uploader;
};

export default createUploader;
