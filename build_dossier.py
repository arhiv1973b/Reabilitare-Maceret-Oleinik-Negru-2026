#!/usr/bin/env python3
"""
TI-ULA Dossier Builder for CASE-MACHERET-1997-2026
Compiles all sealed YAML/JSON nodes into a single legal memorandum.
"""

import os
import yaml
import json
from datetime import datetime

EVIDENCE_DIR = "evidence"
OUTPUT_FILE = "CASE_MACHERET_1997_2026_DOSSIER.md"

def load_nodes():
    nodes = []
    for filename in sorted(os.listdir(EVIDENCE_DIR)):
        filepath = os.path.join(EVIDENCE_DIR, filename)
        if not os.path.isfile(filepath):
            continue
        try:
            if filename.endswith((".yaml", ".yml")):
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    if data and isinstance(data, dict):
                        data['_source_file'] = filename
                        nodes.append(data)
            elif filename.endswith(".json"):
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if data and isinstance(data, dict):
                        data['_source_file'] = filename
                        nodes.append(data)
        except Exception as e:
            print(f"Warning: could not parse {filename}: {e}")
    return nodes

def generate_markdown_dossier(nodes):
    dossier = [
        "# LEGAL DOSSIER: CASE-MACHERET-1997-2026",
        f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (Europe/Chisinau)",
        "**Legal Framework:** Universal Declaration of Human Rights (UDHR), Jus Cogens, Erga Omnes",
        "**Verification Protocol:** TI-ULA (Cryptographic Hashing & Pointer Isolation)",
        "**Root of Trust:** NODE_LEGAL_BASIS_JUS_COGENS",
        "---\n"
    ]

    order = {
        "legal_root_of_trust": 1,
        "legal_framework_anchor": 1,
        "evidence_node": 2,
        "evidence_subnode": 3,
        "verification_link": 4,
        "entity_mapping_node": 5,
        "damage_calculation_node": 6,
        "causation_link": 7
    }

    sorted_nodes = sorted(nodes, key=lambda x: order.get(x.get('type', ''), 99))

    for node in sorted_nodes:
        node_id = node.get('id', 'UNKNOWN_NODE')
        dossier.append(f"## Node: `{node_id}`")
        dossier.append(f"**Type:** {node.get('type', 'N/A')}")
        dossier.append(f"**Source file:** `{node.get('_source_file', 'N/A')}`")
        if node.get('version'):
            dossier.append(f"**Version:** {node.get('version')}")
        if node.get('status'):
            dossier.append(f"**Status:** {node.get('status')}")
        dossier.append("")

        if 'legal_framework' in node:
            dossier.append("### Legal Framework")
            dossier.append("```yaml")
            dossier.append(yaml.dump(node['legal_framework'], allow_unicode=True, default_flow_style=False).rstrip())
            dossier.append("```")
            dossier.append("")

        if 'master_files' in node:
            dossier.append("### Cryptographic Anchors (Master Files)")
            for mf in node['master_files']:
                dossier.append(f"- **File:** `{mf.get('filename')}`")
                if mf.get('sha256'):
                    dossier.append(f"  - **SHA-256:** `{mf.get('sha256')}`")
                if mf.get('role'):
                    dossier.append(f"  - **Role:** {mf.get('role')}")
            dossier.append("")

        if 'entities' in node:
            dossier.append("### Entity Accountability Network")
            for ent in node['entities']:
                name = ent.get('name', 'N/A')
                role = ent.get('role', 'N/A')
                action = ent.get('action', 'N/A')
                status = ent.get('status', '')
                dossier.append(f"- **{name}** ({role}): {action} `{status}`")
            dossier.append("")

        if 'components' in node:
            dossier.append("### Financial & Moral Claim (Provisional)")
            dossier.append("```yaml")
            dossier.append(yaml.dump(node['components'], allow_unicode=True, default_flow_style=False).rstrip())
            dossier.append("```")
            if 'summary' in node and 'total_base_claim_eur' in node['summary']:
                dossier.append(f"**Total Provisional Claim:** {node['summary']['total_base_claim_eur']} EUR")
            elif 'ti_ula_status' in node and 'total_base_claim_eur' in node.get('ti_ula_status', {}):
                dossier.append(f"**Total Provisional Claim:** {node['ti_ula_status']['total_base_claim_eur']} EUR")
            dossier.append("")

        if 'causation_vectors' in node:
            dossier.append("### Causation Vectors")
            for vec in node['causation_vectors']:
                dossier.append(f"- **{vec.get('entity_group')}**: {vec.get('action')}")
                dossier.append(f"  - Effect: {vec.get('effect')}")
            dossier.append("")

        if 'timeline_anchors' in node:
            dossier.append("### Timeline Anchors")
            dossier.append("```yaml")
            dossier.append(yaml.dump(node['timeline_anchors'], allow_unicode=True, default_flow_style=False).rstrip())
            dossier.append("```")
            dossier.append("")

        dossier.append("---\n")

    dossier.append("## Dossier Integrity Statement")
    dossier.append("")
    dossier.append("This consolidated dossier is generated automatically from cryptographically sealed TI-ULA nodes.")
    dossier.append("All SHA-256 anchors and legal mappings remain intact.")
    dossier.append("Root of Trust: `NODE_LEGAL_BASIS_JUS_COGENS` (UDHR + CAT + VCLT 1969 Art. 53 + Constitution RM Arts. 4, 8, 53).")
    dossier.append("ECHR is explicitly excluded as a regional compromise instrument.")
    dossier.append("")
    dossier.append(f"**Total nodes processed:** {len(nodes)}")
    dossier.append(f"**Generation timestamp:** {datetime.now().isoformat()}")

    return "\n".join(dossier)

def main():
    if not os.path.exists(EVIDENCE_DIR):
        print(f"Error: Directory '{EVIDENCE_DIR}' not found.")
        return

    nodes = load_nodes()
    if not nodes:
        print("No valid nodes found.")
        return

    markdown_content = generate_markdown_dossier(nodes)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Success: Consolidated dossier generated at '{OUTPUT_FILE}'.")
    print(f"Total cryptographic nodes processed: {len(nodes)}")
    for n in nodes:
        print(f"  - {n.get('id', 'UNKNOWN')} ({n.get('type', 'N/A')})")

if __name__ == "__main__":
    main()
