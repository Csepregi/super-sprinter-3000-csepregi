
class Functions:

    @staticmethod
    def generate_business_value():
        value_options = []
        for value in range(100, 1500, 100):
            value_options.append(value)
        return value_options

    @staticmethod
    def generate_estimation():
        estimation_options = []
        estimation = 0.5
        while estimation < 40:
            estimation_options.append(estimation)
            estimation += 0.5
        return estimation_options