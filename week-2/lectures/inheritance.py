# 3 ways that the parent and child classes can interact:
# 1. Actions on the child imply an action on the parent.
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the action on the parent.

class Parent():
    def implicit(self):
        print("PARENT implicit")
    
    def override(self):
        print("PARENT override.")
    
    def altered(self):
        print("PARENT altered.")

class Child(Parent):
    def override(self):
        print("CHILD override.")
    
    def altered(self):
        print("CHILD BEFORE PARENT altered.")
        super(Child, self).altered()
        print("CHILD AFTER PARENT altered.")

will_smith = Parent()
will_smith.implicit()
will_smith.override()
will_smith.altered()

jaden_smith = Child()
jaden_smith.implicit()
jaden_smith.override()
jaden_smith.altered()