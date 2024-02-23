#!/usr/bin/python3
"""This is command line interpreter entry."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Define command line interpreter class."""

    prompt = "(hbnb)"

    def __init__(self):
        """Initialize the class_dict in each interpreter."""
        super().__init__()
        self.class_dict = []
        for key, value in storage.objects.items():
            self.class_dict.append(value.__class__)
    
    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Quit the cli on EOF signal."""
        return True

    def emptyline(self):
        """Do not excute anything."""
        return False

    def do_create(self, obj):
        """Create new instance if given class."""
        if obj is None or obj == "":
            print("** class name missing **")
            return
        elif obj not in globals() or not isinstance(globals()[obj], type):
            print("** class doesn't exist **")
            return
        else:
            new_obj = globals()[obj]()
            storage.save()
            print(new_obj.id)

    def do_show(self, args):
        """show the object with id provided."""
        arg =args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return
        else:
            name = arg[0]
        if name not in globals() or not isinstance(globals()[name], type):
            print("** class name missing **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        else:
            ide = arg[1]
            key = "{}.{}".format(name, ide)
            if key not in storage.objects:
                print("** no instance found **")
            else:
                print(str(storage.objects[key]))

    def do_destroy(self, args):
        """Delete an instance of an object class."""
        arg =args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return
        else:
            name = arg[0]
        if name not in globals() or not isinstance(globals()[name], type):
            print("** class name missing **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        else:
            ide = arg[1]
            key = "{}.{}".format(name, ide)
            print(key)
            print(storage.objects)
            if key not in storage.objects:
                print("** no instance found **")
            else:
                """
                new_dict = {}
                for sym, value in storage.objects.items():
                    if sym == key:
                        new_dict[sym] = value
                """
                print("this is a test")
                print(storage.objects)
                print("-------")
                new_dict = storage.objects
                del new_dict[key]
                print(new_dict)
                storage.objects = new_dict
                print("after update")
                print(storage.objects)
                storage.save()

    def do_all(self, *args):
        """print all instances of the name class."""
        name = args[0]
        if name == '' or name is None:
            name = 'BaseModel'
        if name not in globals() or not isinstance(globals()[name], type):
            print("** class doesn't exist **")
            return
        else:
            list = []
            for key, value in storage.objects.items():
                if value.__class__.__name__ == name:
                    list.append(value.__str__())
            print(list)

    def do_update(self, args):
        """Update an attribute of a given class."""
        arg =args.split()
        if len(arg) < 1:
            print("** class name missing **")
            return
        else:
            name = arg[0]
        if name not in globals() or not isinstance(globals()[name], type):
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        else:
            cls_id = arg[1]
        if  len(arg) < 3:
            print("** attribute name missing **")
            return
        else:
            attr = arg[2]

        if len(arg) < 4:
            print("** value missing **")
            return
        else:
            val = arg[3]
        key = "{}.{}".format(name, cls_id)
        if key not in storage.objects:
            print("** no instance found **")
            return
        else:
            obj = storage.objects[key]
            setattr(obj, attr, val)
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
