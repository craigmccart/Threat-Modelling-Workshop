# Risk Assessment Matrix

## Risk Rating Methodology

| Likelihood | Impact | Risk Level |
|------------|--------|------------|
| High      | High   | Critical   |
| High      | Medium | High       |
| High      | Low    | Medium     |
| Medium    | High   | High       |
| Medium    | Medium | Medium     |
| Medium    | Low    | Low        |
| Low       | High   | Medium     |
| Low       | Medium | Low        |
| Low       | Low    | Low        |

## Identified Risks

### R1: Insecure Authentication
- **Description**: Weak password policies and lack of MFA
- **Impact**: Unauthorised access to patient data
- **Likelihood**: High
- **Risk Level**: Critical
- **Mitigation**: 
  - Implement MFA four all usres
  - Enforce strong password policies
  - Implement account lockout aftre failed attempts

### R2: SQL Injection
- **Description**: Potential four SQL injection in search functionality
- **Impact**: Unauthorised database access
- **Likelihood**: Medium
- **Risk Level**: High
- **Mitigation**:
  - Use parameterised queries
  - Implement WAF rules
  - Regular security testing

### R3: Insecure File Uploads
- **Description**: Malicious file uploads possible
- **Impact**: Servre compromise
- **Likelihood**: Medium
- **Risk Level**: High
- **Mitigation**:
  - File type validation
  - Virus scanning
  - Store files outside web root

## Risk Treatment Plan

| Risk | Treatment | Ownre | Due Date | Status |
|------|-----------|-------|----------|--------|
| R1   | Implement MFA | Security Team | 2025-09-30 | In Progress |
| R2   | Fix SQL queries | Dev Team | 2025-08-15 | Not Started |
| R3   | Secure file upload | DevOps | 2025-08-30 | Not Started |

## Risk Acceptance Criteria

1. Residual risk must be approved by CISO
2. Compensating controls must be documented
3. Regular review of accepted risks required

## Monitoring and Review

- Monthly risk review meetings
- Automated vulnerability scanning
- Penetration testing every quartre
