import wx

class FunctionPanel1(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.Button(self, label="Button 1"), 0, wx.ALL, 5)
        sizer.Add(wx.Button(self, label="Button 2"), 0, wx.ALL, 5)
        self.SetSizer(sizer)

class FunctionPanel2(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(wx.StaticText(self, label="Label 1"), 0, wx.ALL, 5)
        sizer.Add(wx.TextCtrl(self), 1, wx.ALL, 5)
        self.SetSizer(sizer)

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None)
        notebook = wx.Notebook(self)

        panel1 = FunctionPanel1(notebook)
        notebook.AddPage(panel1, "Batch Run")

        panel2 = FunctionPanel2(notebook)
        notebook.AddPage(panel2, "Log Check")
        
        panel3 = FunctionPanel2(notebook)
        notebook.AddPage(panel3, "版本保存")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND)
        self.SetSizerAndFit(sizer)
        
        self.SetSize((400, 300))
        self.SetTitle("ToolboX by YZ")
        self.Centre()
        self.Show(True)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
