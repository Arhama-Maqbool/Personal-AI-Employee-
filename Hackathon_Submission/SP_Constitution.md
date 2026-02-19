/sp.constitution # 🏛️ Digital FTE SP Constitution                                                                                                                                    
                                                                                                                                                                                       
  ## Project Name                                                                                                                                                                      
  **Digital FTE v1 – Personal AI Employee**                                                                                                                                            
                                                                                                                                                                                       
  ## Tagline                                                                                                                                                                           
  *Your life and business on autopilot. Local-first, agent-driven, human-in-the-loop.*                                                                                                 
                                                                                                                                                                                       
  ## Objective                                                                                                                                                                         
  Build a fully autonomous Personal AI Employee that:                                                                                                                                  
                                                                                                                                                                                       
  - Operates 24/7                                                                                                                                                                      
  - Manages personal affairs (Gmail, WhatsApp, Bank)                                                                                                                                   
  - Handles business tasks (Social Media, Payments, Project Tasks)                                                                                                                     
  - Uses Claude Code for reasoning and Obsidian for local dashboard                                                                                                                    
                                                                                                                                                                                       
  ## Standout Feature                                                                                                                                                                  
  **Monday Morning CEO Briefing**: Agent autonomously audits financials, tasks, and generates a weekly report.                                                                         
                                                                                                                                                                                       
  ## Architecture                                                                                                                                                                      
  | Component | Purpose |                                                                                                                                                              
  |-----------|---------|                                                                                                                                                              
  | **Brain**: Claude Code | Core reasoning engine with Ralph Wiggum stop hook to iterate until task completion |                                                                      
  | **Memory/GUI**: Obsidian | Local Markdown dashboard for task and knowledge management |                                                                                            
  | **Senses (Watchers)**: Python scripts | Monitor Gmail, WhatsApp, and filesystem for triggers |                                                                                     
  | **Hands (MCP Servers)** | Executes actions (send emails, click buttons) |                                                                                                          
  | **Router** | Routes tasks to the right model (Claude-compatible via OpenRouter Qwen) |                                                                                             
                                                                                                                                                                                       
  ## Tech Stack                                                                                                                                                                        
  - **Python 3.13+**: Watchers & task orchestration                                                                                                                                    
  - **Node.js v24+**: MCP servers & automation                                                                                                                                         
  - **Obsidian v1.10.6+**: Dashboard and local storage                                                                                                                                 
  - **Claude Code**: Reasoning engine                                                                                                                                                  
  - **Github Desktop**: Version control                                                                                                                                                
                                                                                                                                                                                       
  ## Features vs Human FTE                                                                                                                                                             
  | Feature | Human FTE | Digital FTE |
  |---------|-----------|-------------|                                                                                                                                                
  | Availability | 40 hours/week | 168 hours/week |                                                                                                                                    
  | Monthly Cost | $4k – $8k | $500 – $2k |                                                                                                                                            
  | Ramp-up Time | 3–6 months | Instant (via SKILL.md) |                                                                                                                               
  | Consistency | 85–95% | 99%+ |                                                                                                                                                      
  | Scaling | Linear | Exponential |                                                                                                                                                   
  | Annual Hours | ~2,000 | ~8,760 |                                                                                                                                                   
  | Cost per Task | ~$5 | ~$0.25–0.50 |                                                                                                                                                
                                                                                                                                                                                       
  ## Prerequisites                                                                                                                                                                     
  - Claude Code subscription or Free via OpenRouter Qwen                                                                                                                               
  - Obsidian v1.10.6+                                                                                                                                                                  
  - Python 3.13+                                                                                                                                                                       
  - Node.js v24+ LTS                                                                                                                                                                   
  - Github Desktop (version control)                                                                                                                                                   
  - Hardware: Min 8GB RAM, 4-core CPU, 20GB disk                                                                                                                                       
                                                                                                                                                                                       
  ## Setup Checklist                                                                                                                                                                   
  1. Install all required software                                                                                                                                                     
  2. Create Obsidian vault: `AI_