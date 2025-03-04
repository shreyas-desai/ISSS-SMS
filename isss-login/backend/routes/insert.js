import express from "express";
import { format } from 'date-fns';
import {formatInTimeZone }  from 'date-fns-tz';
import path from "path";
import process from "process";
import { authenticate } from "@google-cloud/local-auth";
import { google } from "googleapis";
import { promises as fs } from "fs";

const SCOPES = ["https://www.googleapis.com/auth/spreadsheets"];
const TOKEN_PATH = path.join(process.cwd(), "/backend/token.json");
const CREDENTIALS_PATH = path.join(process.cwd(), "/backend/credentials.json");

async function loadSavedCredentialsIfExist() {
  try {
    const content = await fs.readFile(TOKEN_PATH);
    const credentials = JSON.parse(content);
    return google.auth.fromJSON(credentials);
  } catch (err) {
    return null;
  }
}

function getCurrentESTTime() {
  const now = new Date();
  const estTimeZone = 'America/New_York';
  const estTime = formatInTimeZone(now, estTimeZone,'yyyy-MM-dd HH:mm:ss'); // Convert to EST
  // return format(estTime, 'yyyy-MM-dd HH:mm:ss'); // Format the time
  return estTime
}

async function saveCredentials(client) {
  const content = await fs.readFile(CREDENTIALS_PATH);
  const keys = JSON.parse(content);
  const key = keys.installed || keys.web;
  const payload = JSON.stringify({
    type: "authorized_user",
    client_id: key.client_id,
    client_secret: key.client_secret,
    refresh_token: client.credentials.refresh_token,
  });
  await fs.writeFile(TOKEN_PATH, payload);
}

async function authorize() {
  let client = await loadSavedCredentialsIfExist();
  if (client) {
    return client;
  }
  client = await authenticate({
    scopes: SCOPES,
    keyfilePath: CREDENTIALS_PATH,
  });
  if (client.credentials) {
    await saveCredentials(client);
  }
  return client;
}
async function appendRowToSheet(
  auth,
  firstName,
  lastName,
  cwid,
  email,
  reason
) {
  const sheets = google.sheets({ version: "v4", auth });
  const spreadsheetId = "1UZTk_S5XnEq_9hTmnw-E29SmMfw-nxyuyDlnMf2Rrcg";
  const range = "Sheet1!A:F"; 
  const submittedAt = getCurrentESTTime(); 

  const values = [[firstName, lastName, cwid, email, reason, submittedAt]];
  const resource = { values };

  try {
    const result = await sheets.spreadsheets.values.append({
      spreadsheetId,
      range,
      valueInputOption: "USER_ENTERED", // USER_ENTERED or RAW
      resource,
    });
    console.log(`Row added at: ${result.data.updates.updatedRange}`);
  } catch (error) {
    console.error("Error appending row to sheet:", error);
  }
}

const router = express.Router();

router.route("/").post(async (req, res) => {
  try {
    const { firstName, lastName, cwid, email, reason } = req.body;
    console.log("\t", firstName, lastName, cwid, email, reason, "\t");
    authorize()
      .then((auth) =>
        appendRowToSheet(
          auth,
          firstName,
          lastName,
          cwid,
          email,
          reason
        )
      )
      .catch(console.error);
    res.status(200).json({ success: true });
  } catch (error) {
    console.error("Error submitting form data:", error);
    res.status(500).json({ success: false, error: "Failed to submit data" });
  }
});
export default router;
