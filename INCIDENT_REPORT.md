# [INC-2026-0823] Phishing Triage & Authentication Forensics

## 1. Incident Summary
* **Analyst Name:** [Your Name]
* **Date:** August 23, 2026
* **Severity Level:** High
* **Verdict:** Confirmed Malicious Phishing (Typosquatting & Tor Exit Node Proxy)

## 2. Threat Forensics & Evidence
* **Sender Display Name:** Microsoft Security
* **Spoofed Address:** `no-reply@micros0ft-support.com` (Typosquatted domain using `0` for `o`)
* **Email Authentication:**
  * **SPF:** FAIL (IP `185.220.101.45` not authorized)
  * **DKIM:** FAIL (Signature invalid/missing)
  * **DMARC:** FAIL (Header alignment failed)

## 3. Extracted Indicators of Compromise (IOCs)
| Indicator Type | Value | Context |
|---|---|---|
| **Originating IP** | `185.220.101.45` | Tor Exit Node (`netname: TOR-EXIT`, Germany) |
| **Spoofed Domain** | `micros0ft-support.com` | Typosquatted sender domain |
| **Phishing Domain** | `login-micros0ft.xyz` | Suspicious TLD credential harvesting page |
| **Full URL Payload**| `http://login-micros0ft.xyz/verify?token=abc123` | Phishing URL targeting victim credentials |

## 4. SOC Recommendations & Containment
1. **Perimeter Defense:** Block IP `185.220.101.45` and domain `login-micros0ft.xyz` at the firewall and Secure Email Gateway (SEG).
2. **Mailbox Cleanup:** Purge all emails originating from `@micros0ft-support.com` across the enterprise.
3. **Identity Protection:** Initiate a proactive password reset and enforce MFA for `victim@company.com`.
