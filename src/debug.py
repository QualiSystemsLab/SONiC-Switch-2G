from driver import SonicswitchGen2Driver
import mock
from cloudshell.shell.core.driver_context import ResourceCommandContext, CancellationContext, ConnectivityContext

shell_name = "Sonic Switch 2G"

cancellation_context = mock.create_autospec(CancellationContext)
context = mock.create_autospec(ResourceCommandContext)
context.resource = mock.MagicMock()
context.reservation = mock.MagicMock()
context.connectivity = mock.MagicMock() #mock.create_autospec(ConnectivityContext)
context.reservation.reservation_id = "<RESERVATION_ID>"
context.reservation.domain = "Global"
context.resource.address = "10.3.147.252"
context.resource.name = "SONiC Testing"
context.resource.attributes = dict()
context.resource.attributes["{}.User".format(shell_name)] = "admin"
context.resource.attributes["{}.Password".format(shell_name)] = "password"
#context.resource.attributes["{}.SNMP Read Community".format(shell_name)] = "cHVibGlj"
context.resource.attributes["{}.SNMP Read Community".format(shell_name)] = "dDNzN0xhOA=="
context.resource.attributes["{}.Sessions Concurrency Limit".format(shell_name)] = "1"
context.resource.attributes["{}.CLI Connection Type".format(shell_name)] = "Auto"



driver = SonicswitchGen2Driver()
# print driver.run_custom_command(context, custom_command="sh run", cancellation_context=cancellation_context)
driver.initialize(context)
#driver.get_inventory(context)

with mock.patch('cloudshell.api.cloudshell_api.CloudShellAPISession.__init__', mock.Mock(return_value=None)) as api:
    ret = mock.Mock()
    ret.Value = 't3s7La8'
    with mock.patch('cloudshell.api.cloudshell_api.CloudShellAPISession.DecryptPassword', mock.Mock(return_value=ret)) as decrypt:
        driver.get_inventory(context)

'''with mock.patch('cloudshell.api.cloudshell_api.CloudShellAPISession.__init__', mock.Mock(return_value=None)) as api:
    #driver.set_password(context, "abcdefg")
    driver.delete_user(context)
    #driver.test_commands(context)'''

'''with mock.patch('cloudshell.api.cloudshell_api.CloudShellAPISession.__init__', mock.Mock(return_value=None)) as api:
    ret = mock.Mock()
    ret.Value = 'Cl0udS@213!'
    with mock.patch('cloudshell.api.cloudshell_api.CloudShellAPISession.DecryptPassword', mock.Mock(return_value=ret)) as decrypt:
    #driver.set_password(context, "abcdefg")
    #driver.delete_user(context)
    #driver.test_commands(context)
        driver.orchestration_save(context, "shallow", "")'''