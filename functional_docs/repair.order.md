# BugFix-Studio-Misc — `repair.order`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `repair.order` — Repair Order

*Extends a model created by `repair`.*

Other repos that use this model: `automation Fix-repair.automation_rr_notify_customer_in_ro_end_final` (Fix-repair)<br>`record rule Fix-repair.rule_repair_order_multi_company` (Fix-repair)<br>`server action Fix-repair.action_repair_order_rr_notify_customer_in_ro_end_final` (Fix-repair)<br>`server action Fix-repair.action_rr_add_draft_quotation_confirm_button` (Fix-repair)<br>`server action Fix-repair.action_rr_notify_customer_in_ro_end_final` (Fix-repair)<br>`server action Fix-repair.action_rr_notify_customer_in_ro_end_final_2` (Fix-repair)<br>`server action Fix-repair.action_rr_update_so_in_ro` (Fix-repair)<br>`window action Fix-repair.action_repair_order` (Fix-repair)<details><summary>+1 more</summary>`window action Fix-repair.aw_f4_repair_order_repair_order` (Fix-repair)</details>

**Summary:**

<!-- SUMMARY:model:repair.order -->
This repo only adds eleven PDF letter and document reports for repair orders, C09 to C19. They cover the repair receipt, estimate, quotation, invoice and AOD, a ready-for-collection letter, final notices (standard, estimated, scrappage and estimated scrappage) and a reminder letter. Each uses a copy of the standard repair order report template. No fields or logic are changed.
<!-- /SUMMARY -->

**Reports (11):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Template C09 Repair Receipt | `report_template_c09_repair_receipt` | Prints **Template C09 Repair Receipt** (qweb-pdf) for repair.order records using template `repair.report_repairorder2_copy_1`. | `model repair.order` (repair)<br>`record repair.report_repairorder2_copy_1` (repair) |  |
| Template C10 Repair Estimate | `report_template_c10_repair_estimate` | Prints **Template C10 Repair Estimate** (qweb-pdf) for repair.order records using template `repair.report_repairorder2_copy_2`. | `model repair.order` (repair)<br>`record repair.report_repairorder2_copy_2` (repair) |  |
| Template C11 Repair Quotation | `report_template_c11_repair_quotation` | Prints **Template C11 Repair Quotation** (qweb-pdf) for repair.order records using template `repair.report_repairorder2_copy_3`. | `model repair.order` (repair)<br>`record repair.report_repairorder2_copy_3` (repair) |  |
| Template C12 Repair Invoice | `report_template_c12_repair_invoice` | Prints **Template C12 Repair Invoice** (qweb-pdf) for repair.order records using template `repair.report_repairorder2_copy_4`. | `model repair.order` (repair)<br>`record repair.report_repairorder2_copy_4` (repair) |  |
| Template C13 Repair AOD | `report_template_c13_repair_aod` | Prints **Template C13 Repair AOD** (qweb-pdf) for repair.order records using template `repair.report_repairorder2_copy_5`. | `model repair.order` (repair)<br>`record repair.report_repairorder2_copy_5` (repair) |  |
| Template C14 Ready for collection letter | `report_template_c14_ready_for_collection_letter` | Prints **Template C14 Ready for collection letter** (qweb-pdf) for repair.order records using template `repair.report_repairorder2_copy_6`. | `model repair.order` (repair)<br>`record repair.report_repairorder2_copy_6` (repair) |  |
| Template C15 Final notice | `report_template_c15_final_notice` | Prints **Template C15 Final notice** (qweb-pdf) for repair.order records using template `repair.report_repairorder2_copy_7`. | `model repair.order` (repair)<br>`record repair.report_repairorder2_copy_7` (repair) |  |
| Template C16 Final notice - Estimated | `report_template_c16_final_notice_estimated` | Prints **Template C16 Final notice - Estimated** (qweb-pdf) for repair.order records using template `repair.report_repairorder2_copy_7_copy_1`. | `model repair.order` (repair)<br>`record repair.report_repairorder2_copy_7_copy_1` (repair) |  |
| Template C17 Final notice - Scrappage | `report_template_c17_final_notice_scrappage` | Prints **Template C17 Final notice - Scrappage** (qweb-pdf) for repair.order records using template `repair.report_repairorder2_copy_7_copy_2`. | `model repair.order` (repair)<br>`record repair.report_repairorder2_copy_7_copy_2` (repair) |  |
| Template C18 Final notice - Estimated Scrappage | `report_template_c18_final_notice_estimated_scrappage` | Prints **Template C18 Final notice - Estimated Scrappage** (qweb-pdf) for repair.order records using template `repair.report_repairorder2_copy_7_copy_3`. | `model repair.order` (repair)<br>`record repair.report_repairorder2_copy_7_copy_3` (repair) |  |
| Template C19 Reminder (Repair reminding letter) | `report_template_c19_reminder_repair_reminding_letter` | Prints **Template C19 Reminder (Repair reminding letter)** (qweb-pdf) for repair.order records using template `repair.report_repairorder2_copy_7_copy_4`. | `model repair.order` (repair)<br>`record repair.report_repairorder2_copy_7_copy_4` (repair) |  |
