# galaxy_composite_datatype_test

This is intended to be a small example to test the use of composite data types in Galaxy.  The tool in this case involves running a perl script 'composite_datatype_test.runner.pl', which writes three files:

```
test_file_1.txt
test_file_2.txt
test_file_3.txt
```

which are intended to be incorporated into Galaxy as a composite data type of format 'cdt'.



## To install:

- Edit GALAXY_HOME/config/datatypes_conf.xml  to register the data type:

```
    <datatype extension="cdt" type="galaxy.datatypes.CompositeDataTypeTest:CompositeDataTypeTest" mimetype="text/html" display_in_upload="True" />
```


- Place the 'CompositeDataTypeTest.py' file at GALAXY_HOME/lib/galaxy/datatypes/


- Install the test application
  
   mkdir GALAXY_HOME/tools/test_CDT
   
   cp composite_datatype_test.runner.pl GALAXY_HOME/tools/test_CDT/
   
   cp composite_datatype_test.xml GALAXY_HOME/tools/test_CDT/
   
   and then edit 'GALAXY_HOME/config/tool_conf.xml'  to contain:
   
```
        <section id='test_CDT' name='test_CDT'>
           <tool file='test_CDT/composite_datatype_test.xml' />
        </section>
```

- Fire up galaxy and give it a whirl.
