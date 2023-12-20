require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Cyan
		@button1.Location = System::Drawing::Point.new(84, 285)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(75, 23)
		@button1.TabIndex = 0
		@button1.Text = "button1"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.MediumAquamarine
		@button2.Location = System::Drawing::Point.new(84, 335)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 1
		@button2.Text = "button2"
		@button2.UseVisualStyleBackColor = false
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Purple
		@label1.ForeColor = System::Drawing::Color.HotPink
		@label1.Location = System::Drawing::Point.new(222, 83)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(165, 328)
		@label1.TabIndex = 2
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Pink
		self.ClientSize = System::Drawing::Size.new(975, 463)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.ForeColor = System::Drawing::Color.HotPink
		self.Name = "MainForm"
		self.Text = "schedule"
		self.Load { |sender, e| self.MainFormLoad(sender, e) }
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = " study hall \n Study hall \n Programing \n study hall \n drawing \n painting\n Tc speach"
						 
	end

	def MainFormLoad(sender, e)
		
	end
end

