<div align="center">

  <img src="./banner.png" alt="Rami Tanazefti — Software Engineering, Automation, Cloud and DevOps" width="100%" />

  <a href="https://github.com/NameRami">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=17&duration=2900&pause=1100&color=2DD4BF&center=true&vCenter=true&width=720&lines=I+build+software+that+solves+real+problems.;Full-stack+%C2%B7+Python+automation+%C2%B7+Odoo+ERP;Angular+%C2%B7+Node.js+%C2%B7+Spring+Boot+%C2%B7+.NET;Azure+%C2%B7+Terraform+%C2%B7+Docker+%C2%B7+CI%2FCD" alt="Animated introduction to Rami's engineering focus" />
  </a>

  <br />

  <img src="https://img.shields.io/badge/ISITCOM-Sousse-0F766E?style=flat-square" alt="ISITCOM Sousse" />
  <img src="https://img.shields.io/badge/Based%20in-Tunisia-2563EB?style=flat-square" alt="Based in Tunisia" />
  <img src="https://img.shields.io/badge/Open%20to-PFE%20Internship%202027-16A34A?style=flat-square" alt="Open to a 2027 PFE internship" />

  <br /><br />

  <a href="mailto:ramitanazefti@gmail.com"><img src="https://img.shields.io/badge/Email-ramitanazefti%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Rami" /></a>
  <a href="https://github.com/NameRami?tab=repositories"><img src="https://img.shields.io/badge/All-Repositories-111827?style=for-the-badge&logo=github&logoColor=white" alt="Browse all repositories" /></a>

</div>

---

## Hi, I'm Rami 👋

Final-year **Teleinformatics Engineering** student at **ISITCOM Sousse**, with a bachelor's degree in Software Engineering.

I like taking an idea all the way from **problem → architecture → code → working product**, especially when the result saves someone time, connects two systems, or makes a messy workflow feel simple.

> **How I work:** build for real people, automate the repetitive parts, keep systems understandable.

| | |
|:--|:--|
| 🔭 **Focus** | Full-stack development · business-process automation · data integration · Cloud & DevOps |
| 🏢 **Most recent role** | Software Engineering Intern at **MKG Concept** (Jun–Aug 2026), Odoo ERP integrations in Python and .NET |
| 🎯 **Looking for** | A **2027 end-of-studies (PFE) internship** in software engineering, full-stack, automation/integration, or Cloud & DevOps |
| 🗣️ **Languages** | Arabic (native) · French (advanced) · English (advanced) |

---

## Featured work

### 📰 [NewsroomOS](https://github.com/NameRami/NewsroomOS): full-stack newsroom workspace

One workspace for editorial teams: **news monitoring, publications, internal messaging, live TV monitoring, user management and AI-assisted features**, built on a clean split between frontend, REST API and database.

```mermaid
flowchart LR
  UI["Angular + TypeScript<br/>frontend"] -->|"REST + JWT"| API["Node.js / Express<br/>API"]
  API --> DB[("MongoDB")]
  CI["GitHub Actions CI"] -. "build and test" .-> UI
  CI -. "build and test" .-> API
```

`Angular` · `TypeScript` · `Node.js` · `Express` · `MongoDB` · `JWT` · `GitHub Actions`

**[Read the code →](https://github.com/NameRami/NewsroomOS)**

<br />

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/NameRami/PressRadar">
        <img src="https://raw.githubusercontent.com/NameRami/PressRadar/main/screenshot1.png" alt="PressRadar live news intelligence dashboard" width="100%" />
      </a>
      <h3>🌍 PressRadar</h3>
      <p>Real-time news intelligence dashboard: multiple news sources, a 3D WebGL globe, earthquake and NASA event alerts, and a live TV wall. Ships as a single standalone HTML file.</p>
      <p><code>JavaScript</code> <code>REST APIs</code> <code>Three.js / WebGL</code></p>
      <a href="https://namerami.github.io/PressRadar/PressRadar.html"><b>Live demo ↗</b></a> · <a href="https://github.com/NameRami/PressRadar">Source ↗</a>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/NameRami/LiveTVTower">
        <img src="https://raw.githubusercontent.com/NameRami/LiveTVTower/main/screenshot1.png" alt="LiveTVTower multi-stream television wall" width="100%" />
      </a>
      <h3>📺 LiveTVTower</h3>
      <p>Browser-based TV wall that plays up to nine channels at once, with layouts from 1×1 to 3×3, channel discovery and custom stream playlists. Nothing to install.</p>
      <p><code>HTML</code> <code>CSS</code> <code>JavaScript</code> <code>HLS</code></p>
      <a href="https://namerami.github.io/LiveTVTower/LiveTVTower.html"><b>Live demo ↗</b></a> · <a href="https://github.com/NameRami/LiveTVTower">Source ↗</a>
    </td>
  </tr>
</table>

### ☁️ [Azure Infrastructure as Code](https://github.com/NameRami/terraform-ansible-project)

Terraform definitions for **Azure resources, virtual networking, security configuration and virtual machines**, plus an exploration of the Terraform + Ansible automation workflow.

`Terraform` · `Azure` · `HCL` · `Linux` · `Ansible`

### ⚡ Small tools, useful solutions

| Project | What it does | Stack |
|:--|:--|:--|
| 📋 [**ClipSync**](https://github.com/NameRami/ClipSync) | Syncs clipboard and a shared notepad across devices on the same Wi-Fi | Python · WebSockets · Browser UI |
| 📦 [**QuickShare**](https://github.com/NameRami/QuickShare) | Local file sharing through the browser, with drag-and-drop uploads and QR codes | Python · HTTP |
| 🎯 [**SlideRemote**](https://github.com/NameRami/SlideRemote) | Turns any phone browser into a wireless presentation remote for a Windows PC | Python · WebSockets · Automation |

---

## Experience

**Software Engineering Intern, MKG Concept** · Jun–Aug 2026

I built Python and .NET business tools connected to **Odoo ERP** through **XML-RPC**:

- **Inventory reconciliation:** compares live ERP records with local product data to flag discrepancies and stock-availability problems.
- **Sales analytics:** KPI dashboards covering customer activity, loyalty and monthly trends.
- **Documentation:** technical and user documentation for the tools I delivered.

```mermaid
flowchart LR
  ERP["Odoo ERP<br/>live records"] -->|"XML-RPC"| TOOL["Python / .NET<br/>reconciliation tool"]
  LOCAL["Local product data"] --> TOOL
  TOOL --> OUT["Discrepancy and<br/>stock-availability report"]
```

**Earlier:** IT support, networks and IP surveillance at InfoSelect · 3D modeling and simulation for AI-system evaluation at CRMN · custom automation bots for freelance clients · ERP development exposure at SIMSOFT Technologies.

---

## Tech stack

<table>
  <tr>
    <td width="170"><b>Languages</b></td>
    <td><img src="https://skillicons.dev/icons?i=py,java,cs,js,ts,kotlin,rust,bash&perline=8" alt="Python, Java, C#, JavaScript, TypeScript, Kotlin, Rust, Bash" /></td>
  </tr>
  <tr>
    <td><b>Frontend and mobile</b></td>
    <td><img src="https://skillicons.dev/icons?i=angular,react,nextjs,tailwind,sass,html,css,flutter&perline=8" alt="Angular, React, Next.js, Tailwind CSS, Sass, HTML, CSS, Flutter" /></td>
  </tr>
  <tr>
    <td><b>Backend and APIs</b></td>
    <td><img src="https://skillicons.dev/icons?i=nodejs,express,spring,dotnet,fastapi,prisma,socketio,rabbitmq,kafka&perline=9" alt="Node.js, Express, Spring Boot, .NET, FastAPI, Prisma, Socket.IO, RabbitMQ, Kafka" /></td>
  </tr>
  <tr>
    <td><b>Databases</b></td>
    <td><img src="https://skillicons.dev/icons?i=mongodb,postgres,oracle&perline=8" alt="MongoDB, PostgreSQL, Oracle" /></td>
  </tr>
  <tr>
    <td><b>Cloud and DevOps</b></td>
    <td><img src="https://skillicons.dev/icons?i=azure,aws,terraform,ansible,docker,kubernetes,githubactions,jenkins,gitlab,nginx,linux,git&perline=12" alt="Azure, AWS, Terraform, Ansible, Docker, Kubernetes, GitHub Actions, Jenkins, GitLab, NGINX, Linux, Git" /></td>
  </tr>
  <tr>
    <td><b>AI and automation</b></td>
    <td><img src="https://skillicons.dev/icons?i=ollama,selenium,pandas&perline=8" alt="Ollama, Selenium, Pandas" /><br /><sub>LLMs and AI agents · LangGraph · n8n · Streamlit · Plotly · YOLOv8</sub></td>
  </tr>
  <tr>
    <td><b>ERP and integration</b></td>
    <td><b>Odoo ERP</b> · <b>XML-RPC</b> · Divalto ERP · SQL Server · REST · WebSockets · JWT · data reconciliation</td>
  </tr>
  <tr>
    <td><b>Tools and self-hosting</b></td>
    <td><img src="https://skillicons.dev/icons?i=figma,latex&perline=8" alt="Figma, LaTeX" /><br /><sub>UML · Agile/Scrum · Nextcloud · Nginx Proxy Manager · Uptime Kuma · AdGuard · Jellyfin · LAN and routing</sub></td>
  </tr>
</table>

<sub>Depth varies by technology: the list mixes professional work, coursework, personal projects and hands-on exploration.</sub>

---

## GitHub at a glance

<div align="center">
  <img
    src="https://github-stats-extended.vercel.app/api?username=NameRami&show_icons=true&hide_border=true&bg_color=0D1117&title_color=2DD4BF&icon_color=38BDF8&text_color=C9D1D9"
    alt="Rami's GitHub statistics"
    height="165"
  />
  <img
    src="https://github-stats-extended.vercel.app/api/top-langs/?username=NameRami&layout=compact&hide_border=true&bg_color=0D1117&title_color=2DD4BF&text_color=C9D1D9&langs_count=8"
    alt="Most used programming languages"
    height="165"
  />
</div>

<sub>These cards reflect public repositories only, not everything I have built or used professionally.</sub>

---

<div align="center">

### Let's build something useful

I'm open to **PFE internship opportunities in 2027** and happy to talk about software engineering, full-stack, automation, and Cloud & DevOps projects.

<a href="mailto:ramitanazefti@gmail.com"><img src="https://img.shields.io/badge/Contact%20me-ramitanazefti%40gmail.com-0F766E?style=for-the-badge&logo=gmail&logoColor=white" alt="Email ramitanazefti@gmail.com" /></a>

</div>
