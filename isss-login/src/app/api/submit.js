import { isssData } from "../../lib/mongoConfig";

export default async function handler(req, res) {
    if (req.method === 'POST') {
      try {
        const { firstName, lastName, cwid, email, reason } = req.body;
  
        // Insert the form data into the "submissions" collection
        const result = await isssData.insertOne({
          firstName,
          lastName,
          cwid,
          email,
          reason,
          submittedAt: new Date(),
        });
  
        res.status(200).json({ success: true, data: result });
      } catch (error) {
        console.error("Error submitting form data:", error);
        res.status(500).json({ success: false, error: "Failed to submit data" });
      }
    } else {
      res.status(405).json({ message: "Method not allowed" });
    }
  }