# Table of Contents



 🧙♂ **Tips:** You can also click the TOP RIGHT **table of contents** to read the corresponding section 👉

[1) First use set-up]()

[2) Calibrate the recognizing parameter]()

[3) Start recognizing]()

[4) Program your own project]()

# Color Recognizing Workflow

[1) First use set-up]()

[2) Calibrate the recognizing parameter]()

[3) Start recognizing]()

# 1. First use set-up

## 1.1 Download the Rotrics Vision Terminal

- Mac OS: coming soon
- Windows: https://bit.ly/2GmniPy

## 1.2 Assemble the camera

### 1.2.1 Assemble the left camera mount on the camera.



### 1.2.2 Mount the left part on DexArm and assemble the right part.

![img](https://gblobscdn.gitbook.com/assets%2F-LtPFIBncU5l4J8tl5Yh%2F-MGCvRw4Sru6xlhWyr2Y%2F-MGCxwim-fXCAAg5OSMj%2Fimage.png?alt=media&token=3484ea1b-f2ef-44e7-8586-be6b41fbcf59)

![img](https://gblobscdn.gitbook.com/assets%2F-LtPFIBncU5l4J8tl5Yh%2F-MGDAkz4ZwfRnf_84Qnu%2F-MGDH4icGCkDfE59ghCH%2FSnipaste_2020-09-02_17-45-23.png?alt=media&token=86635828-aeef-4282-b985-6f883b7214dc)

## 1.3 Connect it to your computer

![img](https://gblobscdn.gitbook.com/assets%2F-LtPFIBncU5l4J8tl5Yh%2F-MGDAkz4ZwfRnf_84Qnu%2F-MGDHZYikGnLXWRbcA04%2Fimage.png?alt=media&token=c43047b5-1824-4225-aeeb-59446019168b)

# 2. Calibrate the recognizing parameter

## 2.1 Connect with DexArm and camera

Open Rotrics Vision Terminal and connect with DexArm and camera.

![img](https://gblobscdn.gitbook.com/assets%2F-LtPFIBncU5l4J8tl5Yh%2F-MGDAkz4ZwfRnf_84Qnu%2F-MGDI6MiJEkPgZkjcI6E%2F1.png?alt=media&token=a884cf51-2c1a-439d-bfad-8591004e3619)

Once DexArm has been connected, it will automatically move to the height preview position. You can check the camera's sight area on the **TOP LEFT** image. DexArm couldn't pick up the items that out of the sight area. If you couldn't see all the items in the area, please move DexArm or the items and make sure they are in the sight area.

## 2.2 Choose the demo and adjust the color value.

- Select the **Wood Block Demo** or **Chocolate Bean Demo**.
- Choose the target color.
- Adjust the HSV value until you can see the woodblocks in the **TOP RIGHT** result area.

![img](https://gblobscdn.gitbook.com/assets%2F-LtPFIBncU5l4J8tl5Yh%2F-MGDAkz4ZwfRnf_84Qnu%2F-MGDIEvrL25hHzzOsw8E%2F2.jpg?alt=media&token=1e7ca578-4d0f-439d-b1d3-dc16a0803963)

![img](https://gblobscdn.gitbook.com/assets%2F-LtPFIBncU5l4J8tl5Yh%2F-MGDAkz4ZwfRnf_84Qnu%2F-MGDINtXH3jNCEACuvkg%2F3.gif?alt=media&token=1bac6a41-6fb6-4388-a976-a70e87af0ee8)

## 2.3 Set the target position.

Choose the color and use the DexArm panel to move DexArm to the corresponding place position.

![img](https://gblobscdn.gitbook.com/assets%2F-LtPFIBncU5l4J8tl5Yh%2F-MGDAkz4ZwfRnf_84Qnu%2F-MGDIVaiJhiw5s3mcrAO%2F4.jpg?alt=media&token=184d90ec-e045-4c2c-aec5-6fd0b809c917)



🧙♂ **Tips:** Click **HOME** button every time you set a target position for a new color.

# 3. Start recognizing.

After all color are set, click `**Start** `to run the demo.

If you find that DexArm couldn't pick at the center of the item, try to adjust the XY Multiple values and run again.

![img](https://gblobscdn.gitbook.com/assets%2F-LtPFIBncU5l4J8tl5Yh%2F-MGDAkz4ZwfRnf_84Qnu%2F-MGDIrPZ7a8A0kffIexq%2F5.jpg?alt=media&token=2b6a8e3f-ecb0-4740-9365-ec5847b70c9e)

- X Multiple: the X axis's ratio between image coordinate and DexArm's cartesian coordinate. The value is different in different Z height.
- Y Multiple: the Y axis's ratio between image coordinate and DexArm's cartesian coordinate. The value is different in different Z height.

# 4. Program your own project

Thanks for the continued support from the crowdfunding and maker community, we finally able to bring our dream to life and ship DexArm to you. Now it's time for us to pay back. We've proudly open-sourced the Rotrics Vision Terminal on GitHub, if you are interested in integrating it into your project. You can get the source code on our **GitHub Page**.

Before building your own vision project, please make sure you've learned to program python.

The concept of the Vision Terminal is to use a camera to recognize the items' color and shape. Here are the IDE and tools we use:

- Programming Language: **Python 3.6**
- Python IDE: **Visual Studio Code**
- Image Process Tools: **OpenCV-Python 3.4.1.15**
- Serial Port Communication: **pySerial 3.1**
- Interface Construction: **PyQt5**

The project is built on Visual Studio Code and it's recommended to use the same platform to build it. But you can also use the other Python IDE such as PyCharm, Idle, PyDev to build it.