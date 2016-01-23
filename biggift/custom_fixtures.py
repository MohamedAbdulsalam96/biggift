from __future__ import unicode_literals
import frappe

def get_workflow_action():
	return ['Accept','Approve','Assign to Courier',
			'Assign to Delivery Boy','Assign to Production Team',
			'Assign to Sales Person','Complete','Delivery to Customer','Modify','Reject','Review']

def get_states():
	return [{'Accepted': 'Success'},{'Accepted By Manufacture': 'Primary'},{'Accepted By Production Team': 'Success'}
				,{'Assign to Courier': 'Info'},{'Assign to Delivery Boy': 'Info'}
				,{'Assign to Production Team': 'Info'},{'Assign to Sales Person': 'Info'},{'Customer Accepted': 'Success'}
				,{'Customer Modified': 'Info'},{'Customer Rejected': 'Danger'},{'Customer Reviewed Quotation': 'Info' }
				,{'Customer Reviewed SAS': 'Info'},{'Delivered to Customer': 'Info'}
				,{'Delivered to Customer by Courier': 'Info'},{'Delivered to Customer by Delivery Boy': 'Info'}
				,{'Delivered to Customer by Sales Person': 'Info'},{'QC Accepted': 'Success'}
				,{'QC Rejected': 'Danger'},{'Quotation ready for review': 'Info'},{'Rejected By Production Team': 'Danger'},{'SAS Completed by Production Team': 'Info'}
				,{'Work Order Completed by Production Team': 'Info'}, {'QC Accepted Ready For Dispatch': 'Info'}
				,{'Production Completed':'Success'}]


def get_workflow():
	return {'Pre Order':[{'states': [{'state': 'Assign to Production Team', 'doc_status': 0, 'allow_edit': 'Sales User'}, 
									{'state': 'Accepted By Production Team', 'doc_status': 0, 'allow_edit': 'Manufacturing User'},
									{'state': 'Rejected By Production Team', 'doc_status': 0, 'allow_edit': 'Manufacturing User'},
									{'state': 'Assign to Courier', 'doc_status': 0, 'allow_edit': 'Sales User'},
									{'state': 'Assign to Sales Person', 'doc_status': 0, 'allow_edit': 'Sales User'},
									{'state': 'Assign to Delivery Boy', 'doc_status': 0, 'allow_edit': 'Delivery Boy'},
									{'state': 'Rejected', 'doc_status': 0, 'allow_edit': 'Sales User'},
									{'state': 'Accepted', 'doc_status': 1, 'allow_edit': 'Sales User'},
									{'state': 'Delivered to Customer', 'doc_status': 0, 'allow_edit': 'Sales User'},
									{'state': 'Delivered to Customer by Delivery Boy', 'doc_status': 0, 'allow_edit': 'Delivery Boy'},
									{'state': 'Delivered to Customer by Courier', 'doc_status': 0, 'allow_edit': 'Sales User'},
									{'state': 'Delivered to Customer by Sales Person', 'doc_status': 0, 'allow_edit': 'Sales User'}]},
					{'transitions':[{'state': 'Assign to Production Team', 'action': 'Accept', 'next_state': 'Accepted By Production Team', 'allowed': 'Manufacturing User'},
									{'state': 'Assign to Production Team', 'action': 'Reject', 'next_state': 'Assign to Sales Person', 'allowed': 'Manufacturing User'},
									{'state': 'Accepted By Production Team', 'action': 'Assign to Sales Person', 'next_state': 'Assign to Sales Person', 'allowed': 'Manufacturing User'},
									{'state': 'Accepted By Production Team', 'action': 'Assign to Courier', 'next_state': 'Assign to Courier', 'allowed': 'Manufacturing User'},
									{'state': 'Accepted By Production Team', 'action': 'Assign to Delivery Boy', 'next_state': 'Assign to Delivery Boy', 'allowed': 'Manufacturing User'},
									{'state': 'Assign to Sales Person', 'action': 'Delivery to Customer', 'next_state': 'Delivered to Customer by Sales Person', 'allowed': 'Sales User'},
									{'state': 'Assign to Courier', 'action': 'Delivery to Customer', 'next_state': 'Delivered to Customer by Courier', 'allowed': 'Sales User'},
									{'state': 'Assign to Delivery Boy', 'action': 'Delivery to Customer', 'next_state': 'Delivered to Customer by Delivery Boy', 'allowed': 'Delivery Boy'},
									{'state': 'Delivered to Customer by Sales Person', 'action': 'Accept', 'next_state': 'Accepted', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Sales Person', 'action': 'Modify', 'next_state': 'Assign to Production Team', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Sales Person', 'action': 'Reject', 'next_state': 'Rejected', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Courier', 'action': 'Accept', 'next_state': 'Accepted', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Courier', 'action': 'Modify', 'next_state': 'Assign to Production Team', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Courier', 'action': 'Reject', 'next_state': 'Rejected', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Delivery Boy', 'action': 'Accept', 'next_state': 'Accepted', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Delivery Boy', 'action': 'Modify', 'next_state': 'Assign to Production Team', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Delivery Boy', 'action': 'Reject', 'next_state': 'Rejected', 'allowed': 'Sales User'}
										]}],
			'SAS': [{'states': [{'state': 'Assign to Production Team', 'doc_status': 0, 'allow_edit': 'Manufacturing User'}, 
								{'state': 'SAS Completed by Production Team', 'doc_status': 0, 'allow_edit': 'Manufacturing User'},
								{'state': 'QC Accepted', 'doc_status': 0, 'allow_edit': 'Quality Manager'},
								{'state': 'QC Rejected', 'doc_status': 0, 'allow_edit': 'Manufacturing User'},
								{'state': 'Customer Accepted', 'doc_status': 1, 'allow_edit': 'Sales User'},
								{'state': 'Customer Rejected', 'doc_status': 0, 'allow_edit': 'Manufacturing User'},
								{'state': 'Customer Modified', 'doc_status': 0, 'allow_edit': 'Manufacturing User'},
								{'state': 'Rejected', 'doc_status': 0, 'allow_edit': 'Sales User'},
								{'state': 'Rejected By Production Team', 'doc_status': 0, 'allow_edit': 'Sales User'},
								{'state': 'Customer Reviewed SAS', 'doc_status': 0, 'allow_edit': 'Sales User'},
								{'state': 'Customer Reviewed SAS', 'doc_status': 0, 'allow_edit': 'Sales User'}]},
					{'transitions': [{'state': 'Assign to Production Team', 'action': 'Complete', 'next_state': 'SAS Completed by Production Team', 'allowed': 'Manufacturing User'},
									{'state': 'Assign to Production Team', 'action': 'Complete', 'next_state': 'Rejected By Production Team', 'allowed': 'Manufacturing User'},
									{'state': 'Rejected By Production Team', 'action': 'Assign to Production Team', 'next_state': 'Assign to Production Team', 'allowed': 'Sales User'},
									{'state': 'Rejected By Production Team', 'action': 'Reject', 'next_state': 'Rejected', 'allowed': 'Sales User'},
									{'state': 'SAS Completed by Production Team', 'action': 'Accept', 'next_state': 'QC Accepted', 'allowed': 'Quality Manager'},
									{'state': 'SAS Completed by Production Team', 'action': 'Reject', 'next_state': 'QC Rejected', 'allowed': 'Quality Manager'},
									{'state': 'QC Rejected', 'action': 'Complete', 'next_state': 'SAS Completed by Production Team', 'allowed': 'Manufacturing User'},
									{'state': 'QC Rejected', 'action': 'Reject', 'next_state': 'Rejected', 'allowed': 'Manufacturing User'},
									{'state': 'QC Accepted', 'action': 'Complete', 'next_state': 'Customer Accepted', 'allowed': 'Sales User'},
									{'state': 'QC Accepted', 'action': 'Reject', 'next_state': 'Customer Rejected', 'allowed': 'Sales User'},
									{'state': 'QC Accepted', 'action': 'Modify', 'next_state': 'Customer Modified', 'allowed': 'Sales User'},
									{'state': 'Customer Rejected', 'action': 'Assign to Production Team', 'next_state': 'Assign to Production Team', 'allowed': 'Sales User'},
									{'state': 'Customer Rejected', 'action': 'Reject', 'next_state': 'Rejected', 'allowed': 'Sales User'},
									{'state': 'Customer Modified', 'action': 'Assign to Production Team', 'next_state': 'Assign to Production Team', 'allowed': 'Sales User'},
									{'state': 'Customer Modified', 'action': 'Reject', 'next_state': 'Rejected', 'allowed': 'Sales User'}]}],
			'Work Order': [{'states': [{'state': 'Assign to Production Team', 'doc_status': 0, 'allow_edit': 'Sales User'},
										{'state': 'Accepted By Production Team', 'doc_status': 0, 'allow_edit': 'Manufacturing User'},
										{'state': 'Rejected By Production Team', 'doc_status': 0, 'allow_edit': 'Manufacturing User'},
										{'state': 'Assign to Courier', 'doc_status': 0, 'allow_edit': 'Sales User'},
										{'state': 'Assign to Sales Person', 'doc_status': 0, 'allow_edit': 'Sales User'},
										{'state': 'Assign to Delivery Boy', 'doc_status': 0, 'allow_edit': 'Delivery Boy'},
										{'state': 'Rejected', 'doc_status': 0, 'allow_edit': 'Sales User'},
										{'state': 'Customer Accepted', 'doc_status': 0, 'allow_edit': 'Sales User'},
										{'state': 'Delivered to Customer', 'doc_status': 0, 'allow_edit': 'Sales User'},
										{'state': 'Delivered to Customer by Delivery Boy', 'doc_status': 0, 'allow_edit': 'Delivery Boy'},
										{'state': 'Delivered to Customer by Courier', 'doc_status': 0, 'allow_edit': 'Sales User'},
										{'state': 'Delivered to Customer by Sales Person', 'doc_status': 0, 'allow_edit': 'Sales User'},
										{'state': 'Work Order Completed by Production Team', 'doc_status': 0, 'allow_edit': 'Manufacturing User'},
										{'state': 'QC Accepted', 'doc_status': 0, 'allow_edit': 'Quality Manager'},
										{'state': 'QC Rejected', 'doc_status': 0, 'allow_edit': 'Quality Manager'},
										{'state': 'Customer Rejected', 'doc_status': 0, 'allow_edit': 'Sales User'},
										{'state': 'QC Accepted Ready For Dispatch', 'doc_status': 0, 'allow_edit': 'Sales User'},
										{'state': 'Production Completed', 'doc_status': 1, 'allow_edit': 'Manufacturing User'}]}, 
					{'transitions': [{'state': 'Assign to Production Team', 'action': 'Accept', 'next_state': 'Accepted By Production Team', 'allowed': 'Manufacturing User'},
									{'state': 'Assign to Production Team', 'action': 'Reject', 'next_state': 'Rejected By Production Team', 'allowed': 'Manufacturing User'},
									{'state': 'Rejected By Production Team', 'action': 'Assign to Production Team', 'next_state': 'Assign to Production Team', 'allowed': 'Sales User'},
									{'state': 'Rejected By Production Team', 'action': 'Reject', 'next_state': 'Rejected', 'allowed': 'Sales User'},
									{'state': 'Accepted By Production Team', 'action': 'Complete', 'next_state': 'Work Order Completed by Production Team', 'allowed': 'Manufacturing User'},
									{'state': 'Work Order Completed by Production Team', 'action': 'Accept', 'next_state': 'QC Accepted', 'allowed': 'Quality Manager'},
									{'state': 'Work Order Completed by Production Team', 'action': 'Reject', 'next_state': 'QC Rejected', 'allowed': 'Quality Manager'},
									{'state': 'QC Accepted', 'action': 'Assign to Sales Person', 'next_state': 'Assign to Sales Person', 'allowed': 'Manufacturing User'},
									{'state': 'QC Accepted', 'action': 'Assign to Courier', 'next_state': 'Assign to Courier', 'allowed': 'Manufacturing User'},
									{'state': 'QC Accepted', 'action': 'Assign to Delivery Boy', 'next_state': 'Assign to Delivery Boy', 'allowed': 'Manufacturing User'},
									{'state': 'QC Rejected', 'action': 'Complete', 'next_state': 'Work Order Completed by Production Team', 'allowed': 'Manufacturing User'},
									{'state': 'Assign to Sales Person', 'action': 'Delivery to Customer', 'next_state': 'Delivered to Customer by Sales Person', 'allowed': 'Sales User'},
									{'state': 'Assign to Courier', 'action': 'Delivery to Customer', 'next_state': 'Delivered to Customer by Courier', 'allowed': 'Sales User'},
									{'state': 'Assign to Delivery Boy', 'action': 'Delivery to Customer', 'next_state': 'Delivered to Customer by Delivery Boy', 'allowed': 'Delivery Boy'},
									{'state': 'Delivered to Customer by Sales Person', 'action': 'Accept', 'next_state': 'Customer Accepted', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Sales Person', 'action': 'Reject', 'next_state': 'Customer Rejected', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Sales Person', 'action': 'Assign to Production Team', 'next_state': 'Assign to Production Team', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Courier', 'action': 'Accept', 'next_state': 'Customer Accepted', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Courier', 'action': 'Reject', 'next_state': 'Customer Rejected', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Courier', 'action': 'Assign to Production Team', 'next_state': 'Assign to Production Team', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Delivery Boy', 'action': 'Accept', 'next_state': 'Customer Accepted', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Delivery Boy', 'action': 'Reject', 'next_state': 'Customer Rejected', 'allowed': 'Sales User'},
									{'state': 'Delivered to Customer by Delivery Boy', 'action': 'Assign to Production Team', 'next_state': 'Assign to Production Team', 'allowed': 'Sales User'},
									{'state': 'QC Accepted Ready For Dispatch', 'action': 'Complete', 'next_state': 'Production Completed', 'allowed': 'Manufacturing User'}]
					}],
			'Quotation': [{'states':[{'state': 'Quotation ready for review', 'doc_status': 0, 'allow_edit': 'Sales User'},
									  {'state': 'Customer Accepted', 'doc_status': 1, 'allow_edit': 'Sales User'},
									  {'state': 'Customer Reviewed Quotation', 'doc_status': 0, 'allow_edit': 'Sales User'},
									  {'state': 'Customer Rejected', 'doc_status': 0, 'allow_edit': 'Sales User'},
									  {'state': 'Customer Modified', 'doc_status': 0, 'allow_edit': 'Sales User'},
									  {'state': 'Rejected', 'doc_status': 0, 'allow_edit': 'Sales User'},
									]}, 
					{'transitions':[{'state': 'Customer Reviewed Quotation', 'action': 'Accept', 'next_state': 'Customer Accepted', 'allowed': 'Sales User'},
									{'state': 'Customer Reviewed Quotation', 'action': 'Modify', 'next_state': 'Customer Modified', 'allowed': 'Sales User'},
									{'state': 'Customer Reviewed Quotation', 'action': 'Reject', 'next_state': 'Customer Rejected', 'allowed': 'Sales User'},
									{'state': 'Customer Modified', 'action': 'Complete', 'next_state': 'Quotation ready for review', 'allowed': 'Sales User'},
									{'state': 'Customer Modified', 'action': 'Reject', 'next_state': 'Rejected', 'allowed': 'Sales User'},
									{'state': 'Customer Rejected', 'action': 'Complete', 'next_state': 'Quotation ready for review', 'allowed': 'Sales User'},
									{'state': 'Customer Rejected', 'action': 'Reject', 'next_state': 'Rejected', 'allowed': 'Sales User'}]
					}]}
