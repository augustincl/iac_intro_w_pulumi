from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

#region policy : only in TW
def compute_instance_located_in_tw_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "gcp:compute/instance:Instance":
        zone=args.props["zone"]
        if not zone.startswith("asia-east1"):
            report_violation(f"Expected zone is asia-east1, but the instance is in {zone}")

compute_instance_located_in_tw=ResourceValidationPolicy(
    name="compute_instance_located_in_tw",
    description="Due to the concerns about data privacy and compliance, all compute instances should be located within TW.",
    validate=compute_instance_located_in_tw_validator,
)

#allowed port policy : not allow (> 1024)
def compute_firewall_rule_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "gcp:compute/firewall:Firewall":
        allows=args.props["allows"]
        for rule in allows:
            for port in rule.get("ports"):
                if int(port)>1024:
                    report_violation(f"accessible port number is too big! {port}")

compute_firewall_rule = ResourceValidationPolicy(
    name="compute_firewall_rule",
    description="Accessible port number should not be larger than 1024. If necessary, please confirm the security guy to change the policies for this project",
    validate=compute_firewall_rule_validator,
)

PolicyPack(
    name="intro-policy-check",
    enforcement_level=EnforcementLevel.MANDATORY,
    policies=[
        compute_instance_located_in_tw,
        compute_firewall_rule,
    ],
)
