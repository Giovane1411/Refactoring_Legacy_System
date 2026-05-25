from Hierarchy import (VirtualMachine, DataBase, AutomaticBackup, 
                       FirewallPremium, Support24x7, ResourceGroup ) 

vm = VirtualMachine()
db = DataBase() 


# Cluster Alpha (2 Simple VMs and 1 DataBase)
cluster_alpha = ResourceGroup() # Composite - Starts Empty
cluster_alpha.add_item(vm)
cluster_alpha.add_item(vm)
cluster_alpha.add_item(db)

# Cluster Beta (1 VM + Backup + Firewall)
cluster_beta = ResourceGroup() # Composite - Starts Empty
cluster_beta.add_item(vm)
cluster_beta.add_item(AutomaticBackup(vm))
cluster_beta.add_item(FirewallPremium(vm))

# involved the alpha and beta cluster, then it became a data center.
Main_Data_Center = ResourceGroup()
Main_Data_Center.add_item(cluster_alpha)
Main_Data_Center.add_item(cluster_beta)

# So i involved all of it with Support 24x7
Main_Data_Center = Support24x7(Main_Data_Center)

# Just printing simulation
print(Main_Data_Center.get_price()) 
print(Main_Data_Center.get_description())