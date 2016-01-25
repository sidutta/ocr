#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

void compute_skew(const char* filename)
{
   // Load in grayscale.
   cv::Mat src = cv::imread(filename, 0);
   cv::Size size = src.size();
   cv::bitwise_not(src, src);
    std::vector<cv::Vec4i> lines;
    cv::HoughLinesP(src, lines, 1, CV_PI/180, 100, size.width / 2.f, 20);
    cv::Mat disp_lines(size, CV_8UC1, cv::Scalar(0, 0, 0));
    double angle = 0.;
    unsigned nb_lines = lines.size();
    for (unsigned i = 0; i < nb_lines; ++i)
    {
        cv::line(disp_lines, cv::Point(lines[i][0], lines[i][1]),
                 cv::Point(lines[i][2], lines[i][3]), cv::Scalar(255, 0 ,0));
        angle += atan2((double)lines[i][3] - lines[i][1],
                       (double)lines[i][2] - lines[i][0]);
    }
    angle /= nb_lines; // mean angle, in radians.

    std::cout << "File " << filename << ": " << angle * 180 / CV_PI << std::endl;

    cv::imshow(filename, disp_lines);
    cv::waitKey(0);
    cv::destroyWindow(filename);
}

const char* files[] = {"m8.jpg"};

int main()
{
        unsigned nb_files = sizeof(files) / sizeof(const char*);
        for (unsigned i = 0; i < nb_files; ++i)
                compute_skew(files[i]);
}

