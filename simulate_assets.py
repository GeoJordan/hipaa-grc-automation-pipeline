import pandas as pd
import random

# Set random seed for reproducibility
random.seed(42)

# Define real-world technical pools matching healthcare startup ecosystem
asset_pools = {
    "Network / Remote Access": {
        "names": ["Corporate VPN Gateway", "Production Firewall", "AWS VPC Ingress Route", "Remote Desktop Gateway"],
        "existing_controls": [
            "Single-factor Active Directory password policy.",
            "Standard firewall ingress rules; login attempts logged.",
            "Basic username/password authentication; session timeout after 8 hours."
        ],
        "vulnerabilities": [
            "Lack of Multi-Factor Authentication (MFA) leaves gateway open to credential stuffing.",
            "Weak password policy allows easily guessable credentials on public-facing endpoints.",
            "No geo-fencing or anomalous velocity detection enabled on login attempts."
        ]
    },
    "Data / Database Servers": {
        "names": ["Production PostgreSQL Cluster", "Staging MySQL Database", "AWS S3 ePHI Storage Bucket", "Core EHR Interface Server"],
        "existing_controls": [
            "Developer has authorized corporate network access and valid local machine permissions.",
            "Database access restricted to internal VPC security groups.",
            "Standard backup retention policy enabled; storage encrypted at rest."
        ],
        "vulnerabilities": [
            "Unmasked, live ePHI database backups are copied directly into insecure local dev environments.",
            "Excessive administrative privileges granted to non-production service accounts.",
            "Lack of field-level database encryption or robust database query auditing."
        ]
    },
    "Communication / Email": {
        "names": ["Corporate Email Server (M365)", "Customer Support Ticketing System", "Patient Portal Notification Service", "Outbound SFTP Gateway"],
        "existing_controls": [
            "Opportunistic TLS encryption enabled on the mail server.",
            "Standard inbound spam and phishing email filters active.",
            "Secure web portal links required for internal staff-to-staff messages."
        ],
        "vulnerabilities": [
            "High susceptibility to human error (accidental autocomplete or wrong attachment) via unencrypted email.",
            "Lack of an outbound Email Data Loss Prevention (DLP) engine to scan for ePHI patterns.",
            "No forced encryption gateway rules for external communication with patients/vendors."
        ]
    }
}

# Generate 100 records
data = []
categories = list(asset_pools.keys())

for i in range(1, 101):
    asset_id = f"ASSET-{i:03d}"
    
    # Pick a random category and corresponding asset details
    category = random.choice(categories)
    name = random.choice(asset_pools[category]["names"])
    existing_ctrl = random.choice(asset_pools[category]["existing_controls"])
    vulnerability = random.choice(asset_pools[category]["vulnerabilities"])
    
    data.append({
        "Asset ID": asset_id,
        "Asset Type/Name": f"{name} #{random.randint(1, 5)}",
        "Infrastructure Category": category,
        "Existing Controls": existing_ctrl,
        "Vulnerabilities": vulnerability,
        "Current Risk Rating": "",       # Left blank for manual/automated GRC assessment
        "New Controls": ""               # Left blank for manual/automated GRC assessment
    })

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
output_fn = "simulated_business_infrastructure.csv"
df.to_csv(output_fn, index=False)

print(f"🚀 Successfully simulated 100 business infrastructure records!")
print(f"📊 Saved asset inventory database file to: '{output_fn}'")