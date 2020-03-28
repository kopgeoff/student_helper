import os
import wx


class MyTextDropTarget(wx.TextDropTarget):
    def __init__(self, obj):
        wx.TextDropTarget.__init__(self)
        self.object = obj

    def OnDropText(self, x, y, data):
        try:
            self.object.InsertItem(0, data)
            return True
        except:
            return False


class DragDrop(wx.Frame):
    def __init__(self, parent, ida, title):
        wx.Frame.__init__(self, parent, ida, title, size=(650, 500))

        splitter1 = wx.SplitterWindow(self, -1, style=wx.SP_3D)
        splitter2 = wx.SplitterWindow(splitter1, -1, style=wx.SP_3D)
        splitter1.SetMinimumPaneSize(50)
        splitter2.SetMinimumPaneSize(100)
        self.dir = wx.GenericDirCtrl(splitter1, -1, dir='C:\\', style=wx.DIRCTRL_DIR_ONLY)
        self.lc1 = wx.ListCtrl(splitter2, -1, style=wx.LC_LIST)
        self.lc2 = wx.ListCtrl(splitter2, -1, style=wx.LC_LIST)

        dt = MyTextDropTarget(self.lc2)
        self.lc2.SetDropTarget(dt)
        self.Bind(wx.EVT_LIST_BEGIN_DRAG, self.on_drag_init, id=self.lc1.GetId())

        tree = self.dir.GetTreeCtrl()

        splitter2.SplitHorizontally(self.lc1, self.lc2)
        splitter1.SplitVertically(self.dir, splitter2)

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_select, id=tree.GetId())

        self.on_select(0)
        self.Centre()
        self.Show(True)

    def on_select(self, event):
        list1 = os.listdir(self.dir.GetPath())
        self.lc1.ClearAll()
        self.lc2.ClearAll()
        for i in range(len(list1)):
            if list1[i][0] != '.':
                self.lc1.InsertItem(0, list1[i])
        print(event)

    def on_drag_init(self, event):
        text = self.lc1.GetItemText(event.GetIndex())
        tdo = wx.TextDataObject(text)
        tds = wx.DropSource(self.lc1)
        tds.SetData(tdo)
        tds.DoDragDrop(True)


app = wx.App()
DragDrop(None, -1, 'dragdrop.py')
app.MainLoop()

# 构造一个拖拉对话框, 从网上抄到的https://www.laoyuyu.me/2019/02/14/wxpython/wx_python_9/
# 待添加注释，具体会不会用到另说，要靠这个来学习一些wxpython的知识
