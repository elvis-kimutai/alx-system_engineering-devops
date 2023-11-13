# 0x19. Postmortem
- DevOps
- SysAdmin

# Postmortem: Web Stack Outage Incident

## Issue Summary

### Duration:
 2 hours and 15 minutes, from 9:30 AM to 11:45 AM UTC on November 10, 2023

### Impact:
 The outage affected the main user authentication service, causing login failures and intermittent service availability. Approximately 15% of users were affected during the peak hours.

### Root Cause:
 A misconfiguration in the load balancer settings caused uneven distribution of traffic to the authentication servers, leading to service degradation.

## Timeline

- 9:30 AM UTC: Automated monitoring alerts indicate a spike in authentication errors, triggering the investigation.
- 9:45 AM UTC: Initial investigation focuses on database connectivity and server logs.
- 10:00 AM UTC: Assumed root cause to be a potential DDoS attack due to sudden traffic spikes.
- 10:15 AM UTC: Incident escalated to the DevOps and Security teams for further analysis.
- 11:00 AM UTC: Investigation reveals a misconfiguration in the load balancer settings affecting traffic distribution to the authentication servers.
- 11:30 AM UTC: Load balancer settings are corrected, restoring normal service.
## Misleading Paths

Investigated server hardware issues: This led to unnecessary downtime for non-impacted services.
Explored potential software bugs in the authentication service codebase: This diverted resources from the real issue.
Escalation

The incident was escalated to the DevOps and Security teams at 10:15 AM for further analysis. This was a timely escalation, which helped to resolve the issue more quickly.

## Resolution

The root cause of the outage was identified as a misconfiguration in the load balancer settings. The load balancer settings were adjusted to evenly distribute traffic, ensuring consistent service availability. Additionally, monitoring checks were implemented to detect load balancer misconfigurations promptly.

## Corrective and Preventative Measures

- Conduct regular load balancer configuration audits to prevent misconfigurations.
- Enhance monitoring systems to provide more granular insights into service health and traffic distribution.
- Develop and document a comprehensive incident response plan to streamline the handling of future incidents.
- Provide additional training to the team on debugging misconfigurations in complex systems.
- Schedule regular post-incident reviews to gather insights for continuous improvement.
## Lessons Learned

### The importance of timely escalation
 Escalating the incident to the DevOps and Security teams at 10:15 AM was a critical step in resolving the issue more quickly.
### The need for more granular monitoring
Enhanced monitoring systems that provide more granular insights into service health and traffic distribution could have helped to detect the load balancer misconfiguration earlier.
### The value of incident response plans
Having a comprehensive incident response plan in place would have streamlined the handling of the incident and accelerated the resolution.

## Recommendations

- Implement regular load balancer configuration audits.
- Enhance monitoring systems to provide more granular insights into service health and traffic distribution.
- Develop and document a comprehensive incident response plan.
- Provide additional training to the team on debugging misconfigurations in complex systems.
- Schedule regular post-incident reviews to gather insights for continuous improvement.
