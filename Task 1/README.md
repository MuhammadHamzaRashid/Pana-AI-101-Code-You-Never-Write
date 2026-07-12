# README

## Problem

The objective was to analyze a bank statement to identify any hidden recurring charges or subscription payments. The program detects transactions with the same cleaned description and debit amount occurring more than once, helping highlight potential subscriptions or repeated payments.

## AI Tool Used

ChatGPT was used to generate and explain the Python code for reading the bank statement, cleaning transaction descriptions, identifying duplicate payments, and detecting recurring debit transactions.

## Verification

The results were verified by comparing the detected recurring transactions with the original bank statement. The script correctly identified the recurring **1Bill Invoice** payment of the same amount within the same month, confirming that the recurring payment detection logic worked as expected. No duplicate payments matching the defined criteria (same date, same amount, and same description) were found.
