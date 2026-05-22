import pandas as pd
import os

def analyze_and_chart_compliance():
    input_file = "healthcare_startup_risk_register_100.csv"
    if not os.path.exists(input_file):
        print(f"❌ Error: '{input_file}' not found. Please run your 'inject_vulnerabilities.py' script first.")
        return

    # Load dataframe securely
    df = pd.read_csv(input_file)
    total_assets = int(df.shape[0])
    print(f"📊 Analyzing {total_assets} portfolio assets for regulatory alignment...")

    # Pre-initialize compliance framework tracking columns to prevent index mutation bugs
    df['HIPAA Safeguard Type'] = ""
    df['HIPAA Security Rule Citation'] = ""
    df['HITRUST CSF Category Mapping'] = ""

    # Dynamic Column Finder to automatically locate asset categorization headers
    cat_col = None
    for col in df.columns:
        if "category" in col.lower() or "type" in col.lower():
            cat_col = col
            break
            
    if not cat_col:
        cat_col = df.columns[2] if len(df.columns) > 2 else df.columns[0]

    # Apply framework crosswalk mapping row-by-row based on infrastructure classification
    for idx, row in df.iterrows():
        infra_type = str(row.get(cat_col, '')).lower()
        
        if "network" in infra_type or "vpn" in infra_type or "firewall" in infra_type:
            df.at[idx, 'HIPAA Safeguard Type'] = "Technical (Network)"
            df.at[idx, 'HIPAA Security Rule Citation'] = "45 CFR § 164.312(e)(1) - Transmission Security"
            df.at[idx, 'HITRUST CSF Category Mapping'] = "Category 06.0 - Network & Comm Protection"
            
        elif "data" in infra_type or "postgres" in infra_type or "mysql" in infra_type or "server" in infra_type or "storage" in infra_type or "bucket" in infra_type or "db" in infra_type:
            df.at[idx, 'HIPAA Safeguard Type'] = "Technical/Physical (Data)"
            df.at[idx, 'HIPAA Security Rule Citation'] = "45 CFR § 164.312(a)(1) - Access Control / § 164.310(d)(1)"
            df.at[idx, 'HITRUST CSF Category Mapping'] = "Category 06.c - Protection of Org Records"
            
        else: # Access / Identity / Personnel Endpoints
            df.at[idx, 'HIPAA Safeguard Type'] = "Administrative (Identity)"
            df.at[idx, 'HIPAA Security Rule Citation'] = "45 CFR § 164.308(a)(3) - Workforce Security"
            df.at[idx, 'HITRUST CSF Category Mapping'] = "Category 06.a - User Access Management"

    # Save out the complete, compliance-mapped enterprise portfolio matrix
    matrix_file = "final_portfolio_compliance_matrix_100.csv"
    df.to_csv(matrix_file, index=False)
    print(f"✅ Regulatory matrix successfully compiled and saved to: '{matrix_file}'")

    # Generate Cross-Tabulation Matrix Summary
    print("\n" + "="*70)
    print("📋 EXECUTIVE COMPLIANCE RISK CROSS-TABULATION MATRIX")
    print("="*70)
    
    # Cross-tabulate Safeguard Type vs Current Risk Rating
    cross_tab = pd.crosstab(df['HIPAA Safeguard Type'], df['Current Risk Rating'])
    
    # Enforce clear severity column ordering
    for severity in ['Critical', 'High', 'Medium']:
        if severity not in cross_tab.columns:
            cross_tab[severity] = 0
    cross_tab = cross_tab[['Critical', 'High', 'Medium']]
    cross_tab['Total Gaps'] = cross_tab.sum(axis=1)
    
    # Sort the matrix rows cleanly based on total volume of identified risk gaps
    cross_tab = cross_tab.sort_values(by='Total Gaps', ascending=False)
    print(cross_tab.to_string())
    print("="*70 + "\n")

    # Generate an executive data visualization dashboard using matplotlib & seaborn
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
        
        # Configure charting environments
        sns.set_theme(style="whitegrid")
        plot_df = pd.crosstab(df['HIPAA Safeguard Type'], df['Current Risk Rating'])
        
        for severity in ['Critical', 'High', 'Medium']:
            if severity not in plot_df.columns:
                plot_df[severity] = 0
                
        # Calculate totals to sort chart bars in clean, descending order of magnitude
        plot_df['Total_Count'] = plot_df.sum(axis=1)
        plot_df = plot_df.sort_values(by='Total_Count', ascending=False).drop(columns=['Total_Count'])
        
        # Isolate visual ordering weights (Medium -> High -> Critical stacks vertically)
        plot_df = plot_df[['Medium', 'High', 'Critical']]

        # Render Figure
        ax = plot_df.plot(kind='bar', stacked=True, figsize=(10, 6), 
                          color=['#3498db', '#e67e22', '#c0392b'])
        
        # Graph parameters and label formatting
        plt.title("HIPAA Compliance Gap Breakdown by Safeguard Type and Risk Severity", fontsize=13, fontweight='bold', pad=15)
        plt.xlabel("HIPAA Safeguard Domain", fontsize=11, labelpad=10)
        plt.ylabel("Number of Identified Compliance Gaps", fontsize=11, labelpad=10)
        plt.xticks(rotation=0, fontsize=10)
        plt.yticks(fontsize=10)
        plt.legend(title="Risk Severity", bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=10, title_fontsize=11)
        
        # Dynamically append text label numbers safely onto each stacked bar segment
        for p in ax.patches:
            height = p.get_height()
            x, y = p.get_xy() 
            if height > 0:
                ax.annotate(f'{int(height)}', (x + p.get_width()/2, y + height/2), 
                            ha='center', va='center', color='white', fontweight='bold', fontsize=9)

        plt.tight_layout()
        chart_filename = "compliance_risk_dashboard.png"
        plt.savefig(chart_filename, dpi=300)
        print(f"📈 Executive graphical dashboard rendered and saved to: '{chart_filename}'")
        
    except ImportError:
        print("ℹ️ Note: 'matplotlib' or 'seaborn' libraries not detected locally.")
        print("💡 Tip: To generate the graphic chart asset dashboard, run: pip install matplotlib seaborn")

if __name__ == "__main__":
    analyze_and_chart_compliance()