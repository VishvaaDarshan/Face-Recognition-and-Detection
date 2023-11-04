
# Face Recognition with OpenCV

This project is a simple yet effective demonstration of face detection and recognition using OpenCV.

## Prerequisites

Before getting started, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- OpenCV

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/opencv-face-recognition.git
cd opencv-face-recognition
```

2. Download the Haar Cascade file for face detection and place it in the project directory. You can find it [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).

## Usage

### Step 1: Face Registration

1. Run `t.py` by executing the following command:

```bash
python t.py
```

2. The program will prompt you to enter a number and the name for the respective person whose face you want to register.

3. The program will allocate an area for this person, and the webcam will open for face registration.

### Step 2: Training the Model

1. After registering multiple individuals, you need to run the trainer to create a dataset. Run `trainer.py`:

```bash
python trainer.py
```

2. This will create a dataset for the faces you registered.

### Step 3: Face Recognition

1. Run `main2.py`:

```bash
python main2.py
```

2. The webcam will open, and the program will start recognizing faces from the dataset you created.

## Contributing

Feel free to contribute to this project by making improvements, adding new features, or reporting issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

In your actual repository, make sure to replace "yourusername" with your GitHub username and provide the appropriate links to the Haar Cascade file and license file if necessary.
