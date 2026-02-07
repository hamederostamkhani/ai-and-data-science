from torchvision import transforms


def get_preprocessing_pipeline():
    """
    Returns the preprocessing pipeline used for both training and inference.
    """
    return transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])