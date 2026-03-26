#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    const double c = 3e8;
    const double fs = 1e6;
    const double T = 1e-3;
    const double B = 1e5;
    const double f0 = 1e6;

    const double distance = 100;
    const double velocity = 30;

    const size_t N = static_cast<size_t>(fs * T);
    const double dt = 1.0 / fs;
    const double delay = 2 * distance / c;

    vector<double> tx(N), rx(N), mix(N), time(N);

    for (size_t i = 0; i < N; i++) {
        double t = i * dt;
        time[i] = t;

        tx[i] = sin(2 * M_PI * (f0 * t + (B / (2 * T)) * t * t));

        double t_delayed = t - delay;
        if (t_delayed > 0) {
            double doppler_shift = 2 * velocity * f0 / c;
            rx[i] = sin(2 * M_PI * ((f0 + doppler_shift) * t_delayed + (B / (2 * T)) * t_delayed * t_delayed));
        } else {
            rx[i] = 0;
        }

        mix[i] = tx[i] * rx[i];
    }

    ofstream file("../data/radar_data.csv");
    file << "time,tx,rx,mix\n";
    for (size_t i = 0; i < N; i++)
        file << time[i] << "," << tx[i] << "," << rx[i] << "," << mix[i] << "\n";
    file.close();

    cout << "Data generated successfully.\n";
    return 0;
}
