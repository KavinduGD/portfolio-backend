import { Request, Response } from "express";
import Certificate from "../models/certificateModel";
import asyncHandler from "express-async-handler";
import path from "path";
import fs from "fs/promises";

const getCertificates = asyncHandler(async (req: Request, res: Response) => {
  const certificates = await Certificate.find({});

  const certificatesWithUrls = certificates.map((certificate) => {
    return {
      certificateID: certificate._id,
      name: certificate.name,
      issuer: certificate.issuer,
      issueDate: certificate.issueDate,
      credentialsId: certificate.credentialsId,
      certificateLink: certificate.certificateLink,
      tags: certificate.tags,
      score: certificate.score,
      imageUrl: `${req.protocol}://${req.get("host")}/uploads/certificate/${certificate.certificateImage}`,
    };
  });

  res.status(200).json(certificatesWithUrls);
});

const addCertificate = asyncHandler(async (req: Request, res: Response) => {
  if (!req.file) {
    res.status(400);
    throw new Error("Certificate image is required");
  }

  const {
    name,
    issuer,
    issueDate,
    credentialsId,
    certificateLink,
    tags,
    score,
  } = req.body;

  if (
    !name ||
    !issuer ||
    !issueDate ||
    !credentialsId ||
    !certificateLink ||
    !tags ||
    !score
  ) {
    res.status(400);
    throw new Error("All fields are required");
  }
  const parsedTags = JSON.parse(tags);
  const newCertificate = new Certificate({
    name,
    issuer,
    issueDate,
    credentialsId,
    certificateLink,
    tags: parsedTags,
    score,
    certificateImage: req.file.filename,
  });

  try {
    const savedCertificate = await newCertificate.save();

    res.status(201);
    res.json({
      message: "Certificate added successfully",
      certificate: {
        certificateID: savedCertificate._id,
        name: savedCertificate.name,
        issuer: savedCertificate.issuer,
        issueDate: savedCertificate.issueDate,
        credentialsId: savedCertificate.credentialsId,
        certificateLink: savedCertificate.certificateLink,
        tags: savedCertificate.tags,
        score: savedCertificate.score,
        imageUrl: `${req.protocol}://${req.get("host")}/uploads/certificate/${savedCertificate.certificateImage}`,
      },
    });
  } catch (err) {}
});

const updateCertificate = asyncHandler(async (req: Request, res: Response) => {
  const { id } = req.params;

  const certificate = await Certificate.findById(id);

  if (!certificate) {
    res.status(404);
    throw new Error("Invalid Certificate ID");
  }

  let updates = req.body;
  console.log("updates", updates);

  if (req.file) {
    updates.certificateImage = req.file.filename;
  }

  if (updates.tags) {
    updates.tags = JSON.parse(updates.tags);
  }

  try {
    const updatedCertificate = await Certificate.findByIdAndUpdate(
      id,
      { $set: updates },
      { new: true, runValidators: true },
    );

    // delete the old image is if update is successful
    try {
      if (req.file) {
        const existingImagePath = path.join(
          process.cwd(),
          "uploads",
          "certificate",
          certificate.certificateImage,
        );

        await fs.unlink(existingImagePath);
      }
    } catch (err) {
      res.status(500);
      throw err;
    }

    res.status(200).json({
      message: "Certificate updated successfully",
      certificate: {
        certificateID: updatedCertificate!._id,
        name: updatedCertificate!.name,
        issuer: updatedCertificate!.issuer,
        issueDate: updatedCertificate!.issueDate,
        credentialsId: updatedCertificate!.credentialsId,
        certificateLink: updatedCertificate!.certificateLink,
        tags: updatedCertificate!.tags,
        score: updatedCertificate!.score,
        imageUrl: `${req.protocol}://${req.get("host")}/uploads/certificate/${updatedCertificate!.certificateImage}`,
      },
    });
  } catch (err: any) {
    if (req.file) {
      await fs.unlink(req.file.path);
    }
    res.status(500);
    throw err;
  }
});

const deleteCertificate = asyncHandler(async (req: Request, res: Response) => {
  const { id } = req.params;

  const certificate = await Certificate.findById(id);

  if (!certificate) {
    res.status(404);
    throw new Error("Certificate not found");
  }

  await certificate.deleteOne();

  const imagePath = path.join(
    process.cwd(),
    "uploads",
    "certificate",
    certificate.certificateImage,
  );

  await fs.unlink(imagePath);

  res.status(200).json({
    message: "Certificate deleted successfully",
  });
});

export {
  getCertificates,
  addCertificate,
  updateCertificate,
  deleteCertificate,
};
