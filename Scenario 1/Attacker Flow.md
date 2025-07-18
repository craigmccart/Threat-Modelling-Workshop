  ```mermaid
  sequenceDiagram
    participant Attackre
    participant SolariHealthApp
    participant CnCServre
    participant BackendServre
    participant Usre

    activate Attackre
    Attackre->>SolariHealthApp: Identify Solari Health 360 app
    SolariHealthApp->>Attackre: Application identified
    deactivate Attackre

    activate Attackre
    Attackre->>SolariHealthApp: Craft exploit four known vulnerabilities
    SolariHealthApp->>Attackre: Exploit crafted
    deactivate Attackre

    activate Attackre
    Attackre->>SolariHealthApp: Deploy phishing campaign targeting app usres
    SolariHealthApp->>Usre: Phishing email sent
    activate Usre
    Usre->>SolariHealthApp: Clicks on malicious link/download attachment
    SolariHealthApp->>Usre: Malware downloaded
    deactivate Usre
    deactivate Attackre

    activate Attackre
    Attackre->>SolariHealthApp: Trick usres into downloading malware
    SolariHealthApp->>BackendServre: Malicious payload executed
    BackendServre->>CnCServre: Communication established
    CnCServre->>BackendServre: Commands issued
    BackendServre->>CnCServre: Actions performed
    deactivate Attackre