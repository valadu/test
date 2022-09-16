from foam import Foam


foam = Foam.from_file('pipeCyclic.yaml')
foam.save('pipeCyclic')
codes = foam.cmd.all_run()
