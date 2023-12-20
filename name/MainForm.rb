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
		@button1.Location = System::Drawing::Point.new(244, 164)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(105, 46)
		@button1.TabIndex = 0
		@button1.Text = "show"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(529, 163)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(87, 35)
		@button2.TabIndex = 1
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ActiveCaption
		@label1.Location = System::Drawing::Point.new(244, 13)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(401, 134)
		@label1.TabIndex = 2
		@label1.Text = "label1"
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(1095, 480)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "name"
		self.Load { |sender, e| self.MainFormLoad(sender, e) }
		self.ResumeLayout(false)
	end

	def Label1Click(sender, e)
		
	end

	def Button1Click(sender, e)
		@label1.Text = "Eva White"
	end

	def MainFormLoad(sender, e)
		
	end

	def Button2Click(sender, e)
		@Label1.Text = ""
	end
end

