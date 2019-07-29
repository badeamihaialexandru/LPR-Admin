import tkinter as tk
import tkinter.ttk as ttk

class CheckboxTreeview(ttk.Treeview):
    """
        Treeview widget with checkboxes left of each item.
        The checkboxes are done via the image attribute of the item, so to keep
        the checkbox, you cannot add an image to the item.
    """

    def __init__(self, master=None, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        self.heading("#0",text="Bifeaza",anchor="w")
        self.heading("username",text="Username",anchor="w")

        self.column("#0",width=50)
        self.column("username",width=410)

        # checkboxes are implemented with pictures
        self.im_checked = tk.PhotoImage(file='GUIPhotos/064.png')
        self.im_unchecked = tk.PhotoImage(file='GUIPhotos/063.png')
        self.tag_configure("unchecked", image=self.im_unchecked) #seteaza toate tagurile ce au tagul
                                                                 # unchecked cu imaginea data
        self.tag_configure("checked", image=self.im_checked)
        # check / uncheck boxes on click
        self.bind("<Button-1>", self.box_click, True)



    def insert(self, parent, index, iid=None, **kw):
        """ same method as for standard treeview but add the tag 'unchecked'
            automatically if no tag among ('checked', 'unchecked', 'tristate')
            is given """
        if not "tags" in kw:
            kw["tags"] = ("unchecked",)
        elif not ("unchecked" in kw["tags"] or "checked" in kw["tags"]):
            kw["tags"] = ("unchecked",)
        ttk.Treeview.insert(self, parent, index, iid, **kw)




    def box_click(self, event):
        """ check or uncheck box when clicked """
        x, y, widget = event.x, event.y, event.widget
        elem = widget.identify("element", x, y)
        if "image" in elem:
            item = self.identify_row(y)
            tags = self.item(item, "tags")
            if ("unchecked" in tags):
                self.item(item, tags=("checked",))
                self.tag_configure("checked", background='#0078D7')
            else:
                self.item(item, tags=("unchecked",))
                self.tag_configure("unchecked", background='white')


