"""
Alloy Perceptual Compression Loss
Author: GCP v20 Protocol
Description:
This script implements a perceptual loss function combining MSE, SSIM, LPIPS, and bitrate.
Useful for image compression models that prioritize human perceptual fidelity.
"""

def compute_alloy_loss(mse, ssim, lpips, bitrate, alpha=1.0, beta=1.0, lam=1.0):
    """
    Compute the alloy loss for compression.

    Parameters:
        mse (float): Mean Squared Error
        ssim (float): Structural Similarity Index (0-1)
        lpips (float): Learned Perceptual Image Patch Similarity (0=best)
        bitrate (float): Bits-per-pixel or normalized compression size
        alpha (float): Weight for MSE term
        beta (float): Weight for SSIM term
        lam (float): Weight for LPIPS term

    Returns:
        float: Alloy loss score
    """
    loss = alpha * mse + beta * (1 - ssim) + lam * lpips + bitrate
    return loss


# Example use
if __name__ == "__main__":
    # Dummy image quality metrics
    test_image = {
        "mse": 0.015,
        "ssim": 0.88,
        "lpips": 0.12,
        "bitrate": 0.45
    }

    loss = compute_alloy_loss(**test_image)
    print(f"Alloy Loss: {loss:.4f}")
