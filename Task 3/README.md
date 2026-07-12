This is a short **README** that documents the problem, the technology used, and the verification process for your reconciliation project.

---

# README: Ground Arrangement Collection Reconciliation

## 1. The Problem
The goal was to reconcile a "messy" digital ledger for a ground booking fee. While the bank record showed a total of 5,000 PKR collected, the actual funds available for the ground booking were only 4,000 PKR. 

The complexity arose from two specific "backstage" rules that no standard app could identify:
*   **The Mystery Payer:** A transaction from an unknown number (`0345-XXXX789`) needed to be identified as **Dawood**.
*   **The Debt Filter:** A transaction from **Zahoor** was actually meant to settle a **previous debt**, meaning he had not yet contributed to the current "Ground Arrangement" fund.

The objective was to identify exactly who had paid for the ground, who was still in debt, and provide a clear status for the group.

## 2. AI Tool Used
**Google AI Studio (Gemini)** was used to process the raw data and the human-provided rules. 
*   **The Logic Engine:** The AI was used to build a custom logic flow that prioritizes "Debt Clearance" before "Ground Payment."
*   **The Scripting:** The AI generated a Python script to automate this reconciliation, allowing for "Extra Payment" logic (e.g., if a person pays more than their debt, the remainder is automatically applied to the new collection).

## 3. How the Result Was Verified
Verification was conducted by comparing the AI’s output against the **"Known Answer"** (The Human Private Knowledge):

1.  **Manual Tally:** I established that 5 people x 1,000 = 5,000 PKR total expected.
2.  **Rule Application:** 
    *   I verified that the AI correctly identified the mystery number as **Dawood**.
    *   I verified that the AI **subtracted** Zahoor’s 1,000 from his previous debt rather than counting it toward the ground fund.
3.  **The Mismatch Check:** The AI successfully flagged the "Actionable Mismatch"—showing that even though 5,000 was in the account, Zahoor's ground fee was still missing.
4.  **Mathematical Accuracy:** I confirmed that the final "Message for the Group" accurately reflected the status of all five individuals (4 Paid, 1 Still Owes).

## 4. Conclusion
The reconciliation was successful. By using AI to apply human context to digital records, I was able to turn a messy list of transactions into a clear, actionable summary that identifies exactly who owes what.

---
