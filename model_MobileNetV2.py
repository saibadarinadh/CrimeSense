from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
from glob import glob

# Memory configuration (adjust for GPU usage if needed)
config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.4
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

# Main libraries
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

# Define image size (ensure consistency)
IMAGE_SIZE = (224, 224, 3)  # Adjust for MobileNetV2 input size

# Data paths (double-check accuracy)
train_path = "D://se project//SMARTINTERNZ CRIME//dataset//Train"
valid_path = "D://se project//SMARTINTERNZ CRIME//dataset//Test"

# Load MobileNetV2 (without explicit input_shape)
mobilenet = MobileNetV2(weights='imagenet', include_top=False)

# Freeze pre-trained layers
for layer in mobilenet.layers:
    layer.trainable = False

# Add custom classification head
x = mobilenet.output
x = Flatten()(x)

# Determine number of classes using glob
num_classes = len(glob(train_path + '/*'))

# Dense layer with appropriate number of classes and softmax activation
predictions = Dense(num_classes, activation='softmax')(x)

# Create the model
model = Model(inputs=mobilenet.input, outputs=predictions)

# Compile the model
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(learning_rate=0.0001),  # Lower learning rate
              metrics=['accuracy'])

# Data augmentation (adjust as needed)
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.1,  # Reduced shear
    zoom_range=0.1,  # Reduced zoom
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Load images from directories (consider using flow_from_directory for automatic shape inference)
training_set = train_datagen.flow_from_directory(
    train_path,
    target_size=IMAGE_SIZE[:2],  # Use only height and width
    batch_size=32,
    class_mode='categorical'
)

test_set = test_datagen.flow_from_directory(
    valid_path,
    target_size=IMAGE_SIZE[:2],  # Use only height and width
    batch_size=32,
    class_mode='categorical'
)

# Incorporate shape inference from target_size
total_features = int(np.prod(training_set.target_size) * 3)  # Calculate total features after flattening

# Apply inferred shape to Dense layer
predictions = Dense(num_classes, activation='softmax')(Flatten()(x))

# Train with early stopping and reduced epochs (adjust as needed)
from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(monitor='val_loss', patience=3)

r = model.fit(
    training_set,
    validation_data=test_set,
    epochs=5,  # Start with 5 epochs, increase if needed
    steps_per_epoch=len(training_set),
    validation_steps=len(test_set),
    use_multiprocessing=True,
    workers=4,  # Adjust based on CPU cores
    callbacks=[early_stopping]
)

# Save the model
model.save("crime_detection_model_optimized.h5")
print("Model saved successfully.")
