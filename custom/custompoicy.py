metadata:
  id: "CKV_RM_IMG_01"
  name: "Ensure Kubernetes image should be same"
  category: "Kubernetes Security"

definition:
  cond_type: "attribute"
  resource_types: "all"
  attribute: "spec.template.spec.containers.image"
  operator: "equals"
  value: "nginx"
