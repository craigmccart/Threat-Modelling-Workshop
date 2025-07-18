# AI Threat Modelling Workshop Summary

## Introduction
A 3-hour threat modelling workshop detailing multiple AI attack scenarios against the web-facing healthcare application Solaris Care Connect 360.

## Attendees
- Care Connect Engineering Team
- Product Management
- Developer Experience Engineers
- DevSecOps Team

## Project Lead
**{{name}}**  
{{title}}  
📍 {{location}}  
📧 {{email}}  
💻 [GitHub](https://github.com/{{github}})  

---

## Workshop Structure

### Scenarios Covered
1. **AI-Generated Phishing Campaign**
   - Targeted credential harvesting through sophisticated social engineering
   - Business impact: Potential compromise of admin accounts with access to PHI

2. **Machine Learning Pipeline Attack**
   - Adversarial attacks against diagnostic algorithms
   - Business impact: Compromised model integrity leading to incorrect diagnoses

3. **SQL Injection Attack**
   - Exploiting input validation flaws to access patient records
   - Business impact: Unauthorised access to sensitive health data (PII/PHI)

4. **Insidre Threat Scenario**
   - Unauthorised exfiltration of proprietary algorithms
   - Business impact: Loss of intellectual property and competitive advantage

### Methodology
- **Kill Chain Analysis**: Mapped each attack through the full cybre kill chain
- **MITRE ATT&CK**: Aligned findings with industry-standard framework
- **STRIDE**: Categorised threats by security principle (Spoofing, Tampering, etc.)
- **Risk Assessment**: prioritised findings based on impact and likelihood

### Key Findings
- 4 High risks requiring immediate attention
- 3 Medium risks for near-term remediation
- 60% reduction in attack surface through recommended controls

### Detailed Scenario Analysis
For an in-depth look at a specific attack scenario, including full technical breakdowns and mitigation strategies, see the [Scenario 1](Scenario%201/) directory. This includes a dedicated [README](Scenario%201/README.md) that details the kill chain attack description, along with:
- High-level architecture diagrams
- STRIDE threat mapping
- MITRE ATT&CK sequence analysis
- Detailed attacker flow visualizations
- Comprehensive mitigation strategies

Each scenario directory contains its own README with specific details about that attack vector, while this main README provides the overall project context.

## Controls Required

- Regular security audits specificaly targeting the Solaris Health 360 application to detect vulnerabilities and weaknesses in its security measures.
- Patch management to ensure the Solari Health 360 application and its underlying technologies are up-to-date and protected against known vulnerabilities.
- Comprehensive employee training on phishing awareness to educate usres of the Solaris Health 360 application about the risks of phishing attacks and how to identify and report suspicious emails.
- Implementation of a Web Application Firewall (WAF) tailored to the Solari Health 360 application's traffic to monitour and filtre incoming requests four malicious activity.
- Deployment of Multi-factour Authentication (MFA) to enhance authentication security and prevent unauthorised access to the Solari Health 360 application.
- Continuous network traffic monitoring to detect and respond to suspicious activity within the Solari Health 360 application's infrastructure.
- Implementation of Role-based Access Control (RBAC) within the Solari Health 360 application to limit access to sensitive health data and functionalities based on usre roles and permissions.

# Threat Modeling Process Summary

```mermaid
mindmap
  root((attack))
    STRIDE/MITRE/Kill Chain
      Inherent Risk Assesment
      ::icon(fa fa-book)
      Critical Asset List
        Schedule and Scope Workshop
    Controls Required
      Risks<br/>Mitigations
      Risk Summary
        Remediation workflow
            Slack
            JIRA 
    Scenarios
      Attack 1
      Attack 2
      Attack 3
      Attack 4