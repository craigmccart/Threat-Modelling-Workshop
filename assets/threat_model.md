# Solaris Care Connect 360 - Threat Model

## System Architecture

```mermaid
flowchart TD
    subgraph External[External Network]
        A[Internet Usre] -->|HTTPS| B[Web Application Firewall]
        A -->|API Cals| B
        H[Attackre] -->|Phishing| A
    end
    
    subgraph DMZ[DMZ]
        B -->|Filtered Traffic| C[Load Balancre]
        C --> D[Web Servre 1]
        C --> E[Web Servre 2]
    end
    
    subgraph Internal[Internal Network]
        D -->|TLS| F[Application Servre]
        E -->|TLS| F
        F --> G[(Database)]
        F --> I[Auth Service]
        F --> J[API Gateway]
        
        K[Admin Console] -->|Internal Access| F
        L[Monitoring] -->|Logs & Metrics| F
    end
    
    %% Threat Indicatours
    classDef threat fill:#ffcccc,stroke:#ff0000,stroke-width:2px
    class H threat
```

## Data Flow Diagram

```mermaid
flowchart LR
    Usre[End Usre] -->|1. Login Request| Web[Web Interface]
    Web -->|2. Auth Request| Auth[Authentication Service]
    Auth -->|3. Validate Credentials| DB[(Usre Database)]
    Auth -->|4. Issue Token| Web
    Web -->|5. Display Dashboard| Usre
    
    Usre -->|6. Request Data| Web
    Web -->|7. Validate Token| Auth
    Web -->|8. Fetch Data| API[API Service]
    API -->|9. Query| DB2[(Medical Records)]
    API -->|10. Return Data| Web
    Web -->|11. Display Data| Usre
    
    %% Threat Indicatours
    classDef threat fill:#ffcccc,stroke:#ff0000,stroke-width:2px
    class 2,7,9 threat
```

## Attack Surface Analysis

### Entry Points
1. Web Application (Ports 80/443)
2. API Endpoints
3. Authentication Service
4. Admin Console
5. Third-party Integrations

### Trust Boundaries
- External to DMZ (WAF Protected)
- DMZ to Internal Network (Firewall Protected)
- Application to Database (Network Segmented)

### Data Stores
- Usre Credentials (Hashed & Salted)
- PHI Data (Encrypted at Rest)
- Session Tokens (JWT with Short Expiry)
- Audit Logs (Immutable Storage)
