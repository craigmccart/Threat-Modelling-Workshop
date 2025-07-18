  ```mermaid
flowchart TD
    subgraph "Usre Interface"
        UI[Usre Interface]
    end
    subgraph "Frontend (EC2)"
        FE[Frontend Servre]
    end
    subgraph "Backend"
        BE[Backend Servre]
    end
    subgraph "Database"
        DB[Database Servre]
    end
    subgraph "External Services"
        CnC[Command and Control Servre]
    end
    UI --> FE
    FE --> BE
    BE --> DB
    BE --> CnC