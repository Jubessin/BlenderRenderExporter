import bpy

use_nodes_key = "use_nodes"
surf_node_key = "surf_node"
holdout_exists_key = "holdout_exists"

HoldoutShaderType = "ShaderNodeHoldout"

mat_slots = {}

def attach_holdout(slot, node_tree):
    holdout_output = None
    material_output = node_tree.nodes[0]
    mat_output_input = material_output.inputs[0]
    
    original_surf_node = None
    
    holdout_idx = node_tree.nodes.find("Holdout")
        
    if (holdout_idx == -1):
        mat_slots[slot][holdout_exists_key] = False
        
        holdout_node = node_tree.nodes.new(HoldoutShaderType)
    else:
        mat_slots[slot][holdout_exists_key] = True
        
        holdout_node = node_tree.nodes[holdout_idx]
    
    holdout_output = holdout_node.outputs[0]
    
    if (len(mat_output_input.links) > 0):
        mat_slots[slot][surf_node_key] = mat_output_input.links[0].from_node
    
        if (holdout_output.is_linked and mat_output_input.links[0].from_node == holdout_node):
            return
    else:
        mat_slots[slot][surf_node_key] = None
        
    node_tree.links.new(holdout_output, mat_output_input)
    
def attach_holdout_to_object_materials(obj):
    for slot in obj.material_slots:
        mat_slots[slot] = {}
        mat_slots[slot][use_nodes_key] = slot.material.use_nodes
        
        slot.material.use_nodes = True
        
        attach_holdout(slot, slot.material.node_tree)
        
def remove_holdout_from_object_materials(obj):
    for slot in obj.material_slots:
        node_tree = slot.material.node_tree
        surf_node = mat_slots[slot][surf_node_key]
        mat_output_input = node_tree.nodes[0].inputs[0]
        
        if (surf_node is None or len(mat_output_input.node.inputs[0].links) > 1):
            for link in node_tree.links:
                if (link.to_node.name == "Material Output"):
                    node_tree.links.remove(link)
        else:        
            surf_node_output = surf_node.outputs[0]
        
            node_tree.links.new(surf_node_output, mat_output_input)
        
        slot.material.use_nodes = mat_slots[slot][use_nodes_key]