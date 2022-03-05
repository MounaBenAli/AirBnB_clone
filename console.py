#!/usr/bin/python3
""" program that contains the entry point of the command interpreter"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Simple command processor"""

    prompt = '(hbnb) '

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            create_instance = classes[args[0]]()
            print(create_instance.id)
            create_instance.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation ofan
        instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) == 2:
                key = "{}.{}".format(args[0], args[1])
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) == 2:
                key = "{}.{}".format(args[0], args[1])
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """ Prints all string representation of all
        instances based or not on the class name."""
        args = arg.split()
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            string_list = []
            for value in models.storage.all().values():
                if len(args) > 0 and args[0] == value.__class__.__name__:
                    string_list.append(value.__str__())
                elif len(args) == 0:
                    string_list.append(value.__str__())
            print(string_list)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)."""
        models.storage.reload()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif args[0] in classes:
                if len(args) == 1:
                    print("** instance id missing **")
                    return False
                key = "{}.{}".format(args[0], args[1])
                if key in models.storage.all():
                    dict_to_update = models.storage.all()[key].__dict__
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        k = args[2]
                        try:
                            attrtype = type(dict_to_update[k])
                            v = attrtype(args[3])
                        except KeyError:
                            v = args[3]
                        dict_to_update[k] = v
                        models.storage.save()
                else:
                    print("** no instance found **")

    def do_count(self, arg):
        "Retrieve the number of instances of a given class"
        args = arg.split()
        counter = 0
        for key, value in models.storage.all().items():
            if key.split(".")[0] == args[0]:
                counter += 1
        print(counter)

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Quit command to exit the program\n")

    def default(self, arg):
        """retrieve all instances of a class
        by using: <class name>.instance()."""
        args = arg.split(".")
        if len(args) > 1 and args[0] in classes:
            if args[1] == "all()":
                return self.do_all(args[0])
            elif args[1] == "count()":
                return self.do_count(args[0])
            else:
                print(args[1])
                replace_args = args[1].replace("(", " ").replace(")", "")
                new_args = replace_args.split()
                Cname_id = "{} {}".format(args[0], new_args[1])
                if new_args[0] == "show":
                    return self.do_show(Cname_id)
                elif new_args[0] == "destroy":
                    return self.do_destroy(Cname_id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
