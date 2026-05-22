import pandas as pd
import random

def build_advanced_register():
    asset_file = "simulated_business_infrastructure.csv"
    try:
        df = pd.read_csv(asset_file)
    except FileNotFoundError:
        print(f"❌ Error: '{asset_file}' not found. Run asset simulation script first.")
        return
    except Exception as e:
        print(f"❌ Error reading CSV file: {str(e)}")
        return

    if df is None or len(df.columns) == 0:
        print("❌ Error: The loaded CSV file has no columns or headers.")
        return

    total_records = int(df.shape[0])
    print(f"📊 Successfully loaded database with {total_records} rows.")
    print("🏗️  Translating SRA Audit Context into Live Practical IT Realities...")

    # 🛠️ PRE-INITIALIZE COLUMNS: Explicitly create them so df.at never hits index conversion bugs
    df['Vulnerabilities'] = ""
    df['Current Risk Rating'] = ""
    df['New Controls'] = ""
    df['Existing Controls'] = ""

    # Dynamic Column Finder
    name_col = None
    cat_col = None
    for col in df.columns:
        col_lower = str(col).lower()
        if "name" in col_lower or "asset" in col_lower:
            if name_col is None:
                name_col = col
        if "category" in col_lower or "type" in col_lower:
            cat_col = col

    if not name_col: name_col = df.columns[1] if len(df.columns) > 1 else df.columns[0]
    if not cat_col: cat_col = df.columns[2] if len(df.columns) > 2 else name_col

    print(f"🔍 Mapping using Name Column: '{name_col}' | Category Column: '{cat_col}'")

    # Flat String Lists
    net_issues = ["Compromised VPN Credentials / No MFA", "Ransomware via Exploited RDP", "Insecure Telehealth Sessions", "Unsecured Wi-Fi Usage"]
    net_vulns = ["VPN gateway relies solely on single-factor passwords with no multi-factor validation.", "Open RDP exposure on perimeter firewalls allowing unthrottled brute-force attempts.", "Telehealth privacy failure via peer-to-peer platforms lacking forced encryption.", "Remote personnel accessing clinical systems over public unsecured hot-spots."]
    net_ratings = ["High", "Critical", "Medium", "Medium"]
    net_mitigations = ["Enforce mandatory phishing-resistant MFA across all remote access profiles.", "Disable public-facing RDP; restrict server access behind a VPN gateway.", "Migrate to an enterprise HIPAA-compliant telehealth platform.", "Deploy corporate-managed endpoint VPN clients that enforce auto-encryption."]

    data_issues = ["Engineering copies live production ePHI into dev environments", "Patient scheduling environment encrypted by ransomware", "ePHI cloud storage exposed", "Unencrypted Database Backups"]
    data_vulns = ["Lack of data masking or anonymization pipelines prior to running software application tests.", "Unsupported Operating Systems and missing software patches on critical database servers.", "Cloud misconfiguration leaving storage bucket permissions open to the public internet.", "Database backup jobs dump cleartext files to local attached media without cryptographic protections."]
    data_ratings = ["High", "Critical", "Critical", "High"]
    data_mitigations = ["Implement automated database sanitization/masking scripts.", "Isolate legacy systems within a restricted VLAN and verify daily offline backups.", "Enforce automated cloud compliance guardrails to block public access policies.", "Enable AES-256 bit encryption on all backup destinations."]

    access_issues = ["Long-tenure nurse used valid credentials to access high-profile records", "Terminated Employee Access", "Lost Unencrypted Laptop / Portable Devices", "Shared Privileged Credentials"]
    access_vulns = ["Excessive user permissions and a lack of role-based access control (RBAC) allowing clinical snooping.", "Delayed offboarding processes fail to revoke identity provider and SaaS application access profiles.", "Missing mobile device management (MDM) configuration allowing cleartext drive visibility upon asset loss.", "Multiple operations technicians using a shared administrative 'Admin' account."]
    access_ratings = ["High", "High", "High", "High"]
    access_mitigations = ["Implement strict RBAC restricting chart access based on active patient assignments.", "Establish an automated identity lifecycle sync between HR systems and identity providers.", "Enforce corporate-wide full-disk encryption via centralized MDM policies.", "Decommission shared profiles; enforce individual unique user accounts."]

    # Process dataframe rows safely
    for idx, row in df.iterrows():
        val_name = str(row.get(name_col, '')).lower()
        val_cat = str(row.get(cat_col, '')).lower()
        search_target = f"{val_name} {val_cat}"
        
        r_idx = random.randint(0, 3)
        
        if "network" in search_target or "vpn" in search_target or "firewall" in search_target or "ingress" in search_target:
            issue, vuln, rating, mit = net_issues[r_idx], net_vulns[r_idx], net_ratings[r_idx], net_mitigations[r_idx]
        elif "data" in search_target or "postgres" in search_target or "mysql" in search_target or "server" in search_target or "storage" in search_target or "bucket" in search_target or "db" in search_target:
            issue, vuln, rating, mit = data_issues[r_idx], data_vulns[r_idx], data_ratings[r_idx], data_mitigations[r_idx]
        else:
            issue, vuln, rating, mit = access_issues[r_idx], access_vulns[r_idx], access_ratings[r_idx], access_mitigations[r_idx]
            
        df.at[idx, 'Vulnerabilities'] = vuln
        df.at[idx, 'Current Risk Rating'] = rating
        df.at[idx, 'New Controls'] = mit
        df.at[idx, 'Existing Controls'] = f"Incident Threat Profile: {issue}"

    # Save out the successfully generated production file
    output_filename = "healthcare_startup_risk_register_100.csv"
    df.to_csv(output_filename, index=False)
    
    print("\n✅ Success! Master Portfolio Risk Register Compiled Safely!")
    print(f"📊 Balanced dataset saved to: '{output_filename}'")

if __name__ == "__main__":
    build_advanced_register()